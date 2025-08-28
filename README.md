# PDF-to-Speech Reader (Tkinter + PyPDF2 + pyttsx3)

A tiny desktop-friendly Python script that lets you pick a PDF via the native file dialog and reads it aloud using an offline text‑to‑speech (TTS) engine.

---

## What it does
- Opens a system file picker (Tkinter) to select a `.pdf` file.
- Extracts text from each page (PyPDF2).
- Queues the text and speaks it using the local TTS engine (pyttsx3).
- Exits cleanly if you cancel the file dialog.

---

## Features
- **Offline TTS** (no internet required).
- **Cross‑platform** (Windows/macOS/Linux; uses the OS’s TTS back end).
- **Reads all pages** and speaks them in one continuous pass.
- **Skips empty pages** and guards against missing text.

---

## Requirements
- **Python**: 3.8+
- **Packages**: `pyttsx3`, `PyPDF2` (Tkinter ships with most Python builds)
- **Platform notes**:
  - **Windows**: Uses SAPI5.
  - **macOS**: Uses NSSpeechSynthesizer (built‑in voices).
  - **Linux**: Uses eSpeak/`speech-dispatcher`. You may need to install `espeak-ng` and `python3-tk` via your distro’s package manager.

---

## Installation
```bash
# (optional) create & activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\\Scripts\\activate

# install dependencies
pip install pyttsx3 PyPDF2
```

> **Note (Linux):** If you get TTS backend errors, install your system’s speech engine (e.g., `sudo apt-get install espeak-ng`) and Tk bindings (e.g., `sudo apt-get install python3-tk`).

---

## Usage
1. Save the script as `read_pdf_aloud.py` (or similar).
2. Run it:
   ```bash
   python read_pdf_aloud.py
   ```
3. Choose a PDF in the dialog; the script will begin speaking the text it can extract.

---

## Optional configuration
You can tweak voice, rate, and volume:
```python
engine = pyttsx3.init()
engine.setProperty("rate", 180)     # default is typically ~200
engine.setProperty("volume", 1.0)   # 0.0 to 1.0

# choose a specific voice
voices = engine.getProperty("voices")
for v in voices:
    print(v.id)
engine.setProperty("voice", voices[0].id)
```
Read a page range instead of the whole document:
```python
start, end = 0, 5  # read pages [0..5)
for i in range(start, min(end, len(reader.pages))):
    ...
```

---

## Roadmap (nice‑to‑haves)
- GUI with play/pause, page navigation, progress.
- Page range & chunking long pages for smoother delivery.
- OCR pipeline for scanned PDFs.
- Export to audio file (e.g., WAV/MP3) using pyttsx3’s `save_to_file`.

---

## Credits
- [PyPDF2]
- [pyttsx3]
- Tkinter (Python standard library)

