@echo off
REM ==========================================================================
REM  bench.bat -- read passage.txt in YOUR cloned voice (F5-TTS, local/offline)
REM
REM  Reads:   passage.txt
REM  Voice:   my_voice.wav   (F5-TTS clones the first ~10s)
REM  Writes:  output\yifei_<yyyymmdd_HHMMSS>.wav   (auto-named, then opened)
REM
REM  Usage:   bench.bat
REM
REM  Consent note: only clone a voice you have the right to use (your own, or
REM  a speaker who consented). my_voice.wav is assumed to be yours.
REM ==========================================================================

setlocal
cd /d "%~dp0"

set "PY=.venv-f5\Scripts\python.exe"

if not exist "%PY%" (
    echo [bench] F5 environment missing: %PY%
    echo         Set it up first ^(see README.md / run.bat^).
    exit /b 1
)
if not exist "my_voice.wav" (
    echo [bench] my_voice.wav not found. Record ~15-30s of YOUR OWN voice and
    echo         save it as my_voice.wav in this folder first.
    exit /b 1
)
if not exist "passage.txt" (
    echo [bench] passage.txt not found in this folder.
    exit /b 1
)

echo [bench] Cloning my_voice.wav, reading passage.txt -^> output\yifei_^<timestamp^>.wav
"%PY%" f5_clone.py --reference "my_voice.wav" --text "passage.txt" --out-dir "output" --prefix "yifei_" --open
if errorlevel 1 ( echo [bench] FAILED & exit /b 1 )

echo [bench] Done.
exit /b 0
