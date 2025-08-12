# 🌍 Verfügbare Sprachen

🇬🇧 [English](README.md) | 🇨🇳 [Chinese](README_ZH.md) | 🇪🇸 [Spanish](README_ES.md) | 🇩🇪 [German](README_DE.md) | 🇫🇷 [French](README_FR.md) | 🇮🇹 [Italian](README_IT.md) | 🇵🇹 [Portuguese](README_PT.md) | 🇷🇺 [Russian](README_RU.md) | 🇰🇷 [Korean](README_KO.md) | 🇯🇵 [Japanese](README_JA.md)

---
# 🧠 Whisper Sprache-zu-Text (Offline)

Ein Python-Skript zur automatischen **Spracherkennung aus Audiodateien** mit dem Modell [Whisper](https://github.com/openai/whisper).  
Nach dem Herunterladen und Einrichten wird die Transkription **lokal** auf Ihrem Computer durchgeführt, ohne Daten an einen Server zu senden.

- Recognizes speech in 100+ languages.  
  To list languages, run the script with `--help`.
- Interface language can be selected via `--ui-lang`.  
  Run the script without parameters to see available options.
- Models supported: `tiny`, `base`, `small`, `medium`, `large`.  
  The “larger” the model, the higher the resource requirements — and the better the accuracy.  
  If `--model` is not provided, the script auto-selects a model based on available RAM.
- Provide an audio file via `--file`. Supported formats: `.wav`, `.mp3`, `.m4a`, `.ogg`, etc.  
- Prints a short preview and saves the full text to `output.txt`.

**⚠ Wichtig:**  
Beim ersten Verwenden eines ausgewählten Whisper-Modells wird es automatisch **aus dem Internet heruntergeladen**.  
Model sizes are large — from ~150MB (`tiny`) up to ~3GB (`large`). Stellen Sie eine stabile Internetverbindung und ausreichend Speicherplatz sicher.

---

## 🖥️ Systemanforderungen
- OS: Windows 10/11, Ubuntu 20.04+, macOS 11+  
- RAM: 4GB minimum (16GB recommended for `large`)  
- Disk space: ~6GB free  
- CPU: x86_64 with AVX support (recommended)

📦 After downloading once, the model works entirely offline.

## ✅ Voraussetzungen
- **Python** 3.10  
- **ffmpeg** (audio decoding)  
- **git** (repository cloning)

---

## ⚙️ Installation

### 🪟 Windows

1. Install [Python 3.10](https://www.python.org/downloads/)

2. Install **Git** (https://git-scm.com/download/win) — choose *“Git from the command line”* during setup.

3. Install **ffmpeg**: download from https://ffmpeg.org/download.html, unzip and add `bin/` to `PATH` (or put `ffmpeg.exe` next to the script).

4. Clone the repository:
```bash
git clone https://github.com/avkarcr/audio2text.git
cd audio2text
```

5. Create and activate a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

6. Install dependencies:
```bash
pip install -r requirements.txt
```

---

### 🐧 Linux (Ubuntu/Debian)

1. Install **Python 3.10+**. On Ubuntu 22.04+ it’s preinstalled:
```bash
python3 --version
```

2. Install **git** and **ffmpeg**:
```bash
sudo apt update
sudo apt install git ffmpeg
```

3. Clone the repository:
```bash
git clone https://github.com/avkarcr/audio2text.git
cd audio2text
```

4. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

5. Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 🚀 Verwendung

1. Put `audio.mp3` into the `data/` folder.  
2. Run:
```bash
python main.py
```

📦 The model and file will be selected automatically.  
On first run of a given model, it will be downloaded automatically.

---

## 💡 Beispiele

Run with `medium` model on English (default) with English UI (default):
```bash
python main.py --quiet --file data/audio.mp3 --model medium
```
Run with Korean audio and Korean UI:
```bash
python main.py --quiet --file data/audio.mp3 --model medium --lang ko --ui-lang ko
```
---

## 📄 Ausgabe

📝 Preview of recognized text, full transcription saved to `output.txt`.

---

## ⚠ Hinweise
- Model `large` requires 16+GB RAM.  
- For long audio, prefer at least `medium` model (or split the file with ffmpeg).

---

## 📚 Lizenz
MIT. Uses components of OpenAI [Whisper](https://github.com/openai/whisper).
