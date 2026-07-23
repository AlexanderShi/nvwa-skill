# voice_tts

Read a text passage aloud with a pluggable TTS backend.

## Voice/consent note
This tool clones **only voices you have the right to use** — your own voice, a
speaker who consented, or a licensed/royalty-free clip. It does **not** ship a
real person's voice, and you should not use it to clone a real, identifiable
person without their consent. The default `edge` backend is a fully synthetic
voice (not a real person).

## Quick start (default, no GPU, runs today)
```bash
pip install -r requirements.txt
python tts.py                 # synthesizes passage.txt -> out.mp3
```

Tune the delivery (slower + slightly lower can read as calmer/warmer).
Note: negative values must use `=` so argparse doesn't read them as flags:
```bash
python tts.py --voice zh-CN-XiaoxiaoNeural --rate=-8% --pitch=-2Hz
```

Pick another Chinese voice:
```bash
python -m edge_tts --list-voices | findstr zh-CN
# e.g. zh-CN-XiaoyiNeural, zh-CN-XiaoxiaoNeural, zh-CN-liaoning-XiaobeiNeural
```

Play the result on Windows:
```bash
start out.mp3
```

## Cloning path (your own / consented voice)
Uses ElevenLabs multilingual (handles Chinese). Point it at a reference clip
**you have the rights to** (e.g. your own `my_voice.wav`) — it creates the clone
and synthesizes in one command:
```bash
pip install elevenlabs
setx ELEVENLABS_API_KEY "sk-..."        # then reopen the shell
python tts.py --backend elevenlabs --reference my_voice.wav
```
It prints the new `voice_id`. Reuse it (skips re-cloning) on later runs:
```bash
python tts.py --backend elevenlabs --voice-id <THE_PRINTED_VOICE_ID>
```
Notes:
- 15–60s of clean, single-speaker reference audio works best; your 25 MB clip is plenty.
- Voice cloning requires a paid ElevenLabs plan and its consent verification.

## Files
- `tts.py` — CLI + backends (`edge`, `elevenlabs`)
- `passage.txt` — the text to read
- `requirements.txt` — deps

## Wanting a local, offline clone later?
Models like **CosyVoice 2**, **GPT-SoVITS**, or **F5-TTS** do offline few-shot
cloning with strong Chinese support, but they generally need **Python ≤3.12 +
a CUDA GPU**. If you set up that environment, a third backend can be added with
the same CLI shape. Same consent rule applies.
