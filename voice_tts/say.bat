@echo off
REM Read the current passage.txt aloud in the user's cloned voice.
REM Winning config: CosyVoice2 zero-shot (natural prosody, no prompt-leak with
REM an accurate sidecar transcript), ref_fresh.wav + ref_fresh.txt, speed 0.9.
REM Extra args pass through, e.g.  say.bat --speed 0.85
cd /d "%~dp0"
".venv-cosy\Scripts\python.exe" cosy_clone.py --reference ref_fresh.wav --mode zero_shot --speed 0.9 --open %*
