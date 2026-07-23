"""
Emotional voice cloning with CosyVoice2 (local/offline, GPU).

Unlike F5-TTS (which only copies the reference's flat prosody), CosyVoice2
takes a natural-language *instruction* so you can steer emotion/delivery:

    "用疲惫、温柔、气声的语气，像深夜安慰一个很累的人那样，慢慢地说"

Runs in the dedicated .venv-cosy (Python 3.11). Clones from a reference clip
YOU OWN / HAVE CONSENT TO (same red line as f5_clone.py).

    .venv-cosy\\Scripts\\python.exe cosy_clone.py --instruct "用温柔疲惫的语气慢慢说" --open

First run needs the CosyVoice2-0.5B weights in pretrained_models/CosyVoice2-0.5B
(see download step). ~2 GB, cached after.
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

HERE = Path(__file__).parent
COSY = HERE / "CosyVoice"
# CosyVoice imports its Matcha-TTS submodule by bare path.
sys.path.insert(0, str(COSY))
sys.path.insert(0, str(COSY / "third_party" / "Matcha-TTS"))


def main() -> None:
    ap = argparse.ArgumentParser(description="Emotional voice clone with CosyVoice2.")
    ap.add_argument("--reference", default=str(HERE / "my_voice.wav"),
                    help="Reference clip you own/consent to (timbre source).")
    ap.add_argument("--text", default=str(HERE / "passage.txt"),
                    help="Path to a .txt file, or literal text to speak.")
    ap.add_argument("--instruct",
                    default="用疲惫、温柔、放松的语气，带一点气声，像深夜安慰一个很累的人那样，慢慢地、轻轻地说",
                    help="Natural-language emotion/style instruction (instruct2 mode only).")
    ap.add_argument("--mode", choices=["zero_shot", "cross_lingual", "instruct2"],
                    default="zero_shot",
                    help="zero_shot (clean clone, only speaks the passage; needs --prompt-text) | "
                         "cross_lingual (clone, no transcript needed) | "
                         "instruct2 (text-steered emotion; NOTE: this 0.5B build leaks the "
                         "instruction into the audio, avoid).")
    ap.add_argument("--prompt-text", default="",
                    help="Transcript of --reference (for zero_shot). If empty in zero_shot mode, "
                         "falls back to cross_lingual.")
    ap.add_argument("--model-dir", default=str(COSY / "pretrained_models" / "CosyVoice2-0.5B"),
                    help="CosyVoice2-0.5B weights directory.")
    ap.add_argument("--out", default=None, help="Explicit output path.")
    ap.add_argument("--out-dir", default=str(HERE / "output"))
    ap.add_argument("--prefix", default="yifei_cosy_")
    ap.add_argument("--speed", type=float, default=1.0, help="<1 slower, >1 faster.")
    ap.add_argument("--sentence-pause", type=float, default=0.0,
                    help="Seconds of silence inserted between sentences. When >0, each "
                         "sentence is synthesized separately (cleaner onsets, less slurring) "
                         "and joined with this gap.")
    ap.add_argument("--open", action="store_true", help="Open the file when done (Windows).")
    args = ap.parse_args()

    ref = Path(args.reference)
    if not ref.exists():
        raise SystemExit(f"[error] reference audio not found: {ref}")

    text_path = Path(args.text)
    gen_text = text_path.read_text(encoding="utf-8").strip() if text_path.exists() else args.text
    # CosyVoice's zh frontend handles internal sentence splitting; collapse blank
    # lines so paragraph breaks don't become giant silences.
    gen_text = "\n".join(line for line in (l.strip() for l in gen_text.splitlines()) if line)

    import torch
    import torchaudio
    from cosyvoice.cli.cosyvoice import CosyVoice2

    print(f"[cosy] loading model from {args.model_dir} ...")
    cosyvoice = CosyVoice2(args.model_dir, load_jit=False, load_trt=False, fp16=False)
    sr = cosyvoice.sample_rate
    print(f"[cosy] model loaded, sample_rate={sr}")

    # This CosyVoice2 build loads the prompt internally (at 16k and 24k), so it
    # wants the file PATH, not a pre-loaded tensor.
    prompt_wav = str(ref)

    # Resolve mode. zero_shot needs the reference's transcript to anchor the
    # prompt (an accurate one prevents the model from leaking prompt words into
    # the audio). If --prompt-text is empty, auto-load a sibling <ref>.txt;
    # only fall back to cross_lingual when neither is available.
    mode = args.mode
    prompt_text = args.prompt_text.strip()
    if mode == "zero_shot" and not prompt_text:
        sidecar = ref.with_suffix(".txt")
        if sidecar.exists():
            prompt_text = sidecar.read_text(encoding="utf-8").strip()
            print(f"[cosy] loaded prompt-text from {sidecar.name}")
        else:
            print("[cosy] zero_shot requested but no --prompt-text and no "
                  f"{sidecar.name}; using cross_lingual.")
            mode = "cross_lingual"
    print(f"[cosy] mode={mode}; reference: {ref.name}")

    if args.out:
        out = Path(args.out)
    else:
        from datetime import datetime
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        out = Path(args.out_dir) / f"{args.prefix}{ts}.wav"
    out.parent.mkdir(parents=True, exist_ok=True)

    import re

    def synth(text):
        if mode == "instruct2":
            it = cosyvoice.inference_instruct2(text, args.instruct, prompt_wav, stream=False, speed=args.speed)
        elif mode == "zero_shot":
            it = cosyvoice.inference_zero_shot(text, prompt_text, prompt_wav, stream=False, speed=args.speed)
        else:  # cross_lingual
            it = cosyvoice.inference_cross_lingual(text, prompt_wav, stream=False, speed=args.speed)
        return torch.cat([seg["tts_speech"] for seg in it], dim=1)

    if args.sentence_pause > 0:
        # Split into sentences on CJK/ASCII terminal punctuation, keeping the mark.
        sentences = [s.strip() for s in re.split(r"(?<=[。！？!?…\n])", gen_text) if s.strip()]
        gap = torch.zeros(1, int(sr * args.sentence_pause))
        parts = []
        for idx, s in enumerate(sentences):
            print(f"[cosy] sentence {idx+1}/{len(sentences)}: {s}")
            parts.append(synth(s))
            if idx != len(sentences) - 1:
                parts.append(gap)
        audio = torch.cat(parts, dim=1)
    else:
        audio = synth(gen_text)
    torchaudio.save(str(out), audio, sr)
    print(f"[done] wrote {out.resolve()}  ({audio.shape[1] / sr:.1f}s)")

    if args.open:
        try:
            os.startfile(str(out))  # noqa: S606 (Windows convenience)
        except (AttributeError, OSError):
            pass


if __name__ == "__main__":
    main()
