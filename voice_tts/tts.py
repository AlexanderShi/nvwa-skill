"""
Voice TTS — read a passage aloud with a pluggable TTS backend.

Backends
--------
  edge         Microsoft Edge neural TTS. Synthetic voice (NOT a real person).
               Free, no GPU, great Chinese voices. This is the default.

  elevenlabs   Clone from a reference voice. IMPORTANT: only use a voice you
               have the right to clone — your own voice, a consented speaker,
               or a licensed/royalty-free clip. Do not clone a real,
               identifiable person without their consent.

Usage
-----
  python tts.py                              # edge, default zh voice
  python tts.py --text passage.txt
  python tts.py --voice zh-CN-XiaoxiaoNeural --rate -8%
  python tts.py --backend elevenlabs --voice-id <YOUR_CLONED_VOICE_ID>

List Edge voices:
  python -m edge_tts --list-voices | findstr zh-CN
"""
from __future__ import annotations

import argparse
import asyncio
import os
import sys
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).parent
DEFAULT_TEXT = HERE / "passage.txt"
DEFAULT_OUTDIR = HERE / "output"


def timestamped_out(out: str | None, outdir: str, prefix: str, ext: str) -> Path:
    """Resolve the output path: explicit --out wins; otherwise
    <outdir>/<prefix><yyyymmdd_HHMMSS>.<ext>."""
    if out:
        return Path(out)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    return Path(outdir) / f"{prefix}{ts}.{ext}"


def load_text(text_arg: str | None) -> str:
    if text_arg is None:
        src = DEFAULT_TEXT
    else:
        p = Path(text_arg)
        # If it points at a file, read it; otherwise treat the arg as literal text.
        src = p if p.exists() else None
        if src is None:
            return text_arg
    if not src.exists():
        sys.exit(f"[error] text file not found: {src}")
    return src.read_text(encoding="utf-8").strip()


# --------------------------------------------------------------------------- #
# Backend: Edge (synthetic, default)
# --------------------------------------------------------------------------- #
async def _edge_synth(text: str, out: Path, voice: str, rate: str, pitch: str) -> None:
    import edge_tts

    communicate = edge_tts.Communicate(text, voice=voice, rate=rate, pitch=pitch)
    await communicate.save(str(out))


def _mp3_to_wav(mp3: Path, wav: Path) -> None:
    """Convert MP3 -> WAV using the bundled imageio-ffmpeg binary (no system install)."""
    import subprocess

    import imageio_ffmpeg

    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    subprocess.run(
        [ffmpeg, "-y", "-i", str(mp3), "-ar", "24000", str(wav)],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )


def run_edge(text: str, out: Path, voice: str, rate: str, pitch: str) -> None:
    voice = voice or "zh-CN-XiaoxiaoNeural"  # warm, natural female Mandarin
    print(f"[edge] voice={voice} rate={rate} pitch={pitch}")
    if out.suffix.lower() == ".mp3":
        asyncio.run(_edge_synth(text, out, voice, rate, pitch))
    else:
        # Edge only returns MP3; synth to a temp MP3, then convert to the target.
        tmp = out.with_name(out.stem + ".tmp.mp3")
        asyncio.run(_edge_synth(text, tmp, voice, rate, pitch))
        _mp3_to_wav(tmp, out)
        tmp.unlink(missing_ok=True)


# --------------------------------------------------------------------------- #
# Backend: ElevenLabs (clone from a consented / owned reference voice)
# --------------------------------------------------------------------------- #
def _ivc_create_voice(client, name: str, reference: Path) -> str:
    """Create an Instant Voice Clone from a local reference clip; return voice_id.

    The SDK method name has moved across versions, so try the known spellings.
    """
    if not reference.exists():
        sys.exit(f"[error] reference audio not found: {reference}")

    print(f"[elevenlabs] cloning voice from {reference} ...")
    with open(reference, "rb") as fh:
        files = [fh]
        for attempt in (
            lambda: client.voices.ivc.create(name=name, files=files),  # SDK >= ~1.8
            lambda: client.voices.add(name=name, files=files),          # SDK ~1.x
            lambda: client.clone(name=name, files=files),               # SDK legacy
        ):
            try:
                fh.seek(0)
                voice = attempt()
                break
            except AttributeError:
                voice = None
                continue
        else:
            sys.exit("[error] could not find an IVC method on this SDK version.")

    voice_id = getattr(voice, "voice_id", None) or getattr(voice, "id", None)
    if not voice_id:
        sys.exit(f"[error] clone succeeded but no voice_id returned: {voice!r}")
    print(f"[elevenlabs] created voice_id={voice_id}  (reuse it with --voice-id)")
    return voice_id


def run_elevenlabs(
    text: str, out: Path, voice_id: str | None, reference: str | None, name: str
) -> None:
    from elevenlabs.client import ElevenLabs

    api_key = os.environ.get("ELEVENLABS_API_KEY")
    if not api_key:
        sys.exit("[error] set ELEVENLABS_API_KEY in your environment.")

    client = ElevenLabs(api_key=api_key)

    if not voice_id:
        if not reference:
            sys.exit(
                "[error] pass --reference my_voice.wav to clone a voice you own,\n"
                "        or --voice-id <id> to reuse one you already created."
            )
        voice_id = _ivc_create_voice(client, name, Path(reference))

    print(f"[elevenlabs] synthesizing with voice_id={voice_id}")
    audio = client.text_to_speech.convert(
        voice_id=voice_id,
        model_id="eleven_multilingual_v2",  # handles Chinese
        text=text,
    )
    with open(out, "wb") as f:
        for chunk in audio:
            f.write(chunk)


# --------------------------------------------------------------------------- #
def main() -> None:
    ap = argparse.ArgumentParser(description="Read a passage aloud via a TTS backend.")
    ap.add_argument("--backend", choices=["edge", "elevenlabs"], default="edge")
    ap.add_argument("--text", default=None, help="Path to a .txt file, or literal text.")
    ap.add_argument("--out", default=None,
                    help="Explicit output path. If omitted, auto-names into --out-dir.")
    ap.add_argument("--out-dir", default=str(DEFAULT_OUTDIR), help="Folder for auto-named output.")
    ap.add_argument("--prefix", default="yifei_", help="Filename prefix for auto-named output.")
    ap.add_argument("--open", action="store_true", help="Open the file when done (Windows).")
    ap.add_argument("--voice", default="", help="Edge voice name.")
    ap.add_argument("--rate", default="+0%", help="Edge speaking rate, e.g. -8%%.")
    ap.add_argument("--pitch", default="+0Hz", help="Edge pitch, e.g. -2Hz.")
    ap.add_argument("--voice-id", default=None, help="Reuse an existing cloned voice id.")
    ap.add_argument("--reference", default=None,
                    help="Local reference clip to clone (a voice you own/consent to), e.g. my_voice.wav")
    ap.add_argument("--name", default="my_cloned_voice", help="Name for the created clone.")
    args = ap.parse_args()

    text = load_text(args.text)
    ext = "wav" if args.backend == "edge" else "mp3"
    out = timestamped_out(args.out, args.out_dir, args.prefix, ext)
    out.parent.mkdir(parents=True, exist_ok=True)

    if args.backend == "edge":
        run_edge(text, out, args.voice, args.rate, args.pitch)
    else:
        run_elevenlabs(text, out, args.voice_id, args.reference, args.name)

    print(f"[done] wrote {out.resolve()}  ({out.stat().st_size} bytes)")
    if args.open:
        try:
            os.startfile(str(out))  # noqa: S606 (Windows-only convenience)
        except (AttributeError, OSError):
            pass


if __name__ == "__main__":
    main()
