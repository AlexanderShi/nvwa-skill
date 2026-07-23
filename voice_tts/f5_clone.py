"""
Local, free, offline voice cloning with F5-TTS.

Runs in the dedicated .venv-f5 (Python 3.11) environment, NOT your system
Python. Clones from a reference clip YOU OWN / HAVE CONSENT TO.

    .venv-f5\\Scripts\\python.exe f5_clone.py                 # clone my_voice.wav
    .venv-f5\\Scripts\\python.exe f5_clone.py --ref-text "写在这里可省去自动转写"

First run downloads the F5TTS_v1_Base weights + vocoder (~1.3 GB), cached after.
On CPU, generating the passage takes ~1-3 minutes.
"""
from __future__ import annotations

import argparse
import os
import shutil
from pathlib import Path

HERE = Path(__file__).parent


def _ensure_ffmpeg_on_path() -> None:
    """F5's auto-transcribe (transformers) shells out to a bare `ffmpeg`.

    Expose the bundled imageio-ffmpeg binary as `ffmpeg.exe` on PATH so no
    system install is needed. No-op if a real ffmpeg is already present.
    """
    if shutil.which("ffmpeg"):
        return
    try:
        import imageio_ffmpeg
    except ImportError:
        return
    src = Path(imageio_ffmpeg.get_ffmpeg_exe())
    bindir = HERE / "ffbin"
    bindir.mkdir(exist_ok=True)
    dst = bindir / "ffmpeg.exe"
    if not dst.exists():
        shutil.copy(src, dst)
    os.environ["PATH"] = str(bindir) + os.pathsep + os.environ.get("PATH", "")


_ensure_ffmpeg_on_path()


def main() -> None:
    ap = argparse.ArgumentParser(description="Clone a voice you own with F5-TTS (local/offline).")
    ap.add_argument("--reference", default=str(HERE / "my_voice.wav"),
                    help="Reference clip you own/consent to (uses first ~15s).")
    ap.add_argument("--ref-text", default="",
                    help="Transcript of the reference. Empty = auto-transcribe.")
    ap.add_argument("--text", default=str(HERE / "passage.txt"),
                    help="Path to a .txt file, or literal text to speak.")
    ap.add_argument("--out", default=None,
                    help="Explicit output path. If omitted, auto-names into --out-dir.")
    ap.add_argument("--out-dir", default=str(HERE / "output"), help="Folder for auto-named output.")
    ap.add_argument("--prefix", default="yifei_", help="Filename prefix for auto-named output.")
    ap.add_argument("--open", action="store_true", help="Open the file when done (Windows).")
    ap.add_argument("--speed", type=float, default=1.0, help="<1 slower, >1 faster.")
    ap.add_argument("--nfe-step", type=int, default=32,
                    help="Diffusion steps. Higher = smoother/cleaner, slower. 32=default, 48-64=nicer.")
    ap.add_argument("--cross-fade", type=float, default=0.15,
                    help="Crossfade seconds between generated chunks. Higher = less 'separate sentences'.")
    ap.add_argument("--cfg", type=float, default=2.0, help="Guidance strength (adherence to ref).")
    ap.add_argument("--sway", type=float, default=-1.0, help="Sway sampling coefficient.")
    args = ap.parse_args()

    ref = Path(args.reference)
    if not ref.exists():
        raise SystemExit(f"[error] reference audio not found: {ref}")

    text_path = Path(args.text)
    gen_text = text_path.read_text(encoding="utf-8").strip() if text_path.exists() else args.text

    # F5 wants a short reference (<~15s) + its transcript. We prepare a clean
    # ~10s mono clip and, if no transcript was given, transcribe it ourselves by
    # feeding a numpy array to Whisper — which avoids torchaudio/torchcodec file
    # decoding (broken on this Windows CPU stack) entirely.
    ref_clip = HERE / "ref_clip.wav"
    ref_text = args.ref_text
    clip_seconds = 10.0

    import numpy as np
    import soundfile as sf

    data, sr = sf.read(str(ref), dtype="float32")
    if data.ndim > 1:                       # stereo -> mono
        data = data.mean(axis=1)
    data = data[: int(clip_seconds * sr)]   # first ~10s
    sf.write(str(ref_clip), data, sr)
    print(f"[f5] prepared {clip_seconds:.0f}s mono reference -> {ref_clip.name} (sr={sr})")

    import torch

    device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype = torch.float16 if device == "cuda" else torch.float32
    print(f"[f5] device={device} dtype={dtype}")

    if not ref_text:
        print("[f5] transcribing reference (direct model, no pipeline/torchcodec) ...")
        import torchaudio.functional as AF
        from transformers import WhisperForConditionalGeneration, WhisperProcessor

        # Call the model directly on a mel spectrogram we compute from the numpy
        # array. This skips transformers' ASR *pipeline*, whose preprocess step
        # hard-imports torchcodec (unloadable on this Windows stack).
        model_id = "openai/whisper-large-v3-turbo"
        processor = WhisperProcessor.from_pretrained(model_id)
        model = WhisperForConditionalGeneration.from_pretrained(model_id)
        model = model.to(device=device, dtype=dtype)
        model.eval()

        wav16 = AF.resample(torch.from_numpy(data), sr, 16000).numpy()
        feats = processor(wav16, sampling_rate=16000, return_tensors="pt").input_features
        feats = feats.to(device=device, dtype=dtype)
        with torch.no_grad():
            ids = model.generate(feats, language="zh", task="transcribe", max_new_tokens=256)
        ref_text = processor.batch_decode(ids, skip_special_tokens=True)[0].strip()
        print(f"[f5] reference transcript: {ref_text!r}")

    from f5_tts.api import F5TTS

    print("[f5] loading model (first run downloads ~1.3 GB) ...")
    f5 = F5TTS(device=device)  # F5TTS_v1_Base — multilingual EN/ZH

    if args.out:
        out = Path(args.out)
    else:
        from datetime import datetime
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        out = Path(args.out_dir) / f"{args.prefix}{ts}.wav"
    out.parent.mkdir(parents=True, exist_ok=True)

    print(f"[f5] cloning from {ref_clip.name}")
    f5.infer(
        ref_file=str(ref_clip),
        ref_text=ref_text,               # explicit -> F5 skips its auto-transcriber
        gen_text=gen_text,
        file_wave=str(out),
        speed=args.speed,
        nfe_step=args.nfe_step,
        cross_fade_duration=args.cross_fade,
        cfg_strength=args.cfg,
        sway_sampling_coef=args.sway,
        remove_silence=False,            # avoids an ffmpeg dependency
    )
    print(f"[done] wrote {out.resolve()}")
    if args.open:
        try:
            os.startfile(str(out))  # noqa: S606 (Windows-only convenience)
        except (AttributeError, OSError):
            pass


if __name__ == "__main__":
    main()
