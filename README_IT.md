# 🌍 Lingue Disponibili

🇬🇧 [Inglese](README.md) | 🇨🇳 [Cinese](README_ZH.md) | 🇪🇸 [Spagnolo](README_ES.md) | 🇩🇪 [Tedesco](README_DE.md) | 🇫🇷 [Francese](README_FR.md) | 🇮🇹 [Italiano](README_IT.md) | 🇵🇹 [Portoghese](README_PT.md) | 🇷🇺 [Russo](README_RU.md) | 🇰🇷 [Coreano](README_KO.md) | 🇯🇵 [Giapponese](README_JA.md)

---
# 🧠 Whisper Speech-to-Text (Offline)

Uno script Python per il **riconoscimento automatico della voce da file audio** utilizzando il modello [Whisper](https://github.com/openai/whisper).  
Dopo il download e la configurazione, la trascrizione viene eseguita **localmente** sul tuo computer senza inviare dati a nessun server.

- Riconosce la voce in oltre 100 lingue.  
  Per elencare le lingue, esegui lo script con `--help`.
- La lingua dell'interfaccia può essere selezionata con `--ui-lang`.  
  Esegui lo script senza parametri per vedere le opzioni disponibili.
- Modelli supportati: `tiny`, `base`, `small`, `medium`, `large`.  
  Più il modello è “grande”, maggiori sono i requisiti di risorse — e migliore sarà l'accuratezza.  
  Se `--model` non è specificato, lo script seleziona automaticamente un modello in base alla RAM disponibile.
- Fornisci un file audio con `--file`. Formati supportati: `.wav`, `.mp3`, `.m4a`, `.ogg`, ecc.  
- Mostra un'anteprima breve e salva il testo completo in `output.txt`.

**⚠ Importante:**  
Al primo utilizzo di un modello Whisper selezionato, questo verrà **scaricato da Internet** automaticamente.  
Le dimensioni dei modelli sono elevate — da ~150MB (`tiny`) fino a ~3GB (`large`). Assicurati di avere una connessione stabile e spazio su disco sufficiente.

---

## 🖥️ Requisiti di Sistema
- OS: Windows 10/11, Ubuntu 20.04+, macOS 11+  
- RAM: minimo 4GB (16GB consigliati per `large`)  
- Spazio su disco: ~6GB liberi  
- CPU: x86_64 con supporto AVX (consigliato)

📦 Dopo il primo download, il modello funziona completamente offline.

## ✅ Requisiti
- **Python** 3.10  
- **ffmpeg** (decodifica audio)  
- **git** (clonazione repository)

---

## ⚙️ Installazione

### 🪟 Windows

1. Installa [Python 3.10](https://www.python.org/downloads/)

2. Installa **Git** (https://git-scm.com/download/win) — scegli *“Git from the command line”* durante l'installazione.

3. Installa **ffmpeg**: scarica da https://ffmpeg.org/download.html, estrai e aggiungi `bin/` al `PATH` (oppure posiziona `ffmpeg.exe` accanto allo script).

4. Clona il repository:
```bash
git clone https://github.com/avkarcr/audio2text.git
cd audio2text
```

5. Crea e attiva un ambiente virtuale:
```bash
python -m venv venv
venv\Scripts\activate
```

6. Installa le dipendenze:
```bash
pip install -r requirements.txt
```

---

### 🐧 Linux (Ubuntu/Debian)

1. Installa **Python 3.10+**. Su Ubuntu 22.04+ è preinstallato:
```bash
python3 --version
```

2. Installa **git** e **ffmpeg**:
```bash
sudo apt update
sudo apt install git ffmpeg
```

3. Clona il repository:
```bash
git clone https://github.com/avkarcr/audio2text.git
cd audio2text
```

4. Crea e attiva un ambiente virtuale:
```bash
python3 -m venv venv
source venv/bin/activate
```

5. Installa le dipendenze:
```bash
pip install -r requirements.txt
```

---

## 🚀 Utilizzo

1. Metti `audio.mp3` nella cartella `data/`.  
2. Esegui:
```bash
python main.py
```

📦 Il modello e il file saranno selezionati automaticamente.  
Al primo avvio di un modello, verrà scaricato automaticamente.

---

## 💡 Esempi

Esegui con il modello `medium` in inglese (default) con interfaccia in inglese (default):
```bash
python main.py --quiet --file data/audio.mp3 --model medium
```
Esegui con audio in coreano e interfaccia in coreano:
```bash
python main.py --quiet --file data/audio.mp3 --model medium --lang ko --ui-lang ko
```

---

## 📄 Output

📝 Anteprima del testo riconosciuto, trascrizione completa salvata in `output.txt`.

---

## ⚠ Note
- Il modello `large` richiede almeno 16GB di RAM.  
- Per audio lunghi, si consiglia almeno il modello `medium` (o dividere il file con ffmpeg).

---

## 📚 Licenza
MIT. Utilizza componenti di OpenAI [Whisper](https://github.com/openai/whisper).
