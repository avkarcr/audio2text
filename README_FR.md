# 🌍 Langues disponibles

🇬🇧 [Anglais](README.md) | 🇨🇳 [Chinois](README_ZH.md) | 🇪🇸 [Espagnol](README_ES.md) | 🇩🇪 [Allemand](README_DE.md) | 🇫🇷 [Français](README_FR.md) | 🇮🇹 [Italien](README_IT.md) | 🇵🇹 [Portugais](README_PT.md) | 🇷🇺 [Russe](README_RU.md) | 🇰🇷 [Coréen](README_KO.md) | 🇯🇵 [Japonais](README_JA.md)

---
# 🧠 Whisper Speech-to-Text (Hors ligne)

Un script Python pour la **reconnaissance vocale automatique à partir de fichiers audio** utilisant le modèle [Whisper](https://github.com/openai/whisper).  
Après téléchargement et configuration, la transcription est effectuée **localement** sur votre ordinateur sans envoyer de données à un serveur.

- Reconnaît la parole dans plus de 100 langues.  
  Pour lister les langues, exécutez le script avec l’option --help.
- La langue de l’interface peut être sélectionnée via --ui-lang.  
  Exécutez le script sans paramètres pour voir les options disponibles.
- Modèles pris en charge : tiny, base, small, medium, large.  
  Plus le modèle est "grand", plus il est exigeant en ressources — et meilleure est la précision.  
  Si l’option --model n’est pas fournie, le script sélectionne automatiquement un modèle en fonction de la RAM disponible.
- Fournissez un fichier audio via --file. Formats pris en charge : .wav, .mp3, .m4a, .ogg, etc.  
- Affiche un aperçu court et enregistre le texte complet dans output.txt.

**⚠ Important :**  
Lors de la première utilisation d’un modèle Whisper sélectionné, il sera **téléchargé automatiquement depuis Internet**.  
La taille des modèles est importante — d’environ 150 Mo (tiny) à environ 3 Go (large). Assurez-vous d’avoir une connexion stable et suffisamment d’espace disque.

---

## 🖥️ Configuration système requise
- OS : Windows 10/11, Ubuntu 20.04+, macOS 11+  
- RAM : minimum 4 Go (16 Go recommandés pour large)  
- Espace disque : ~6 Go libres  
- CPU : x86_64 avec support AVX (recommandé)

📦 Après le premier téléchargement, le modèle fonctionne entièrement hors ligne.

## ✅ Prérequis
- **Python** 3.10  
- **ffmpeg** (décodage audio)  
- **git** (clonage du dépôt)

---

## ⚙️ Installation

### 🪟 Windows

1. Installer [Python 3.10](https://www.python.org/downloads/)

2. Installer **Git** (https://git-scm.com/download/win) — choisissez “Git from the command line” pendant l’installation.

3. Installer **ffmpeg** : téléchargez depuis https://ffmpeg.org/download.html, décompressez et ajoutez `bin/` au `PATH` (ou placez `ffmpeg.exe` à côté du script).

4. Cloner le dépôt :
```bash
git clone https://github.com/avkarcr/audio2text.git
cd audio2text
```

5. Créer et activer un environnement virtuel :
```bash
python -m venv venv
venv\Scripts\activate
```

6. Installer les dépendances :
```bash
pip install -r requirements.txt
```

---

### 🐧 Linux (Ubuntu/Debian)

1. Installer **Python 3.10+**. Sur Ubuntu 22.04+ il est déjà installé :
```bash
python3 --version
```

2. Installer **git** et **ffmpeg** :
```bash
sudo apt update
sudo apt install git ffmpeg
```

3. Cloner le dépôt :
```bash
git clone https://github.com/avkarcr/audio2text.git
cd audio2text
```

4. Créer et activer un environnement virtuel :
```bash
python3 -m venv venv
source venv/bin/activate
```

5. Installer les dépendances :
```bash
pip install -r requirements.txt
```

---

## 🚀 Utilisation

1. Mettre `audio.mp3` dans le dossier `data/`.  
2. Lancer :
```bash
python main.py
```

📦 Le modèle et le fichier seront sélectionnés automatiquement.  
Lors de la première utilisation, le modèle sera téléchargé automatiquement.

---

## 💡 Exemples

Exécuter avec le modèle medium en anglais (par défaut) et interface en anglais (par défaut) :
```bash
python main.py --quiet --file data/audio.mp3 --model medium
```
Exécuter avec un audio coréen et interface en coréen :
```bash
python main.py --quiet --file data/audio.mp3 --model medium --lang ko --ui-lang ko
```

---

## 📄 Résultat

📝 Aperçu du texte reconnu, transcription complète enregistrée dans `output.txt`.

---

## ⚠ Remarques
- Le modèle large nécessite 16+ Go de RAM.  
- Pour les fichiers audio longs, privilégiez au moins le modèle medium (ou découpez le fichier avec ffmpeg).

---

## 📚 Licence
MIT. Utilise des composants de [Whisper](https://github.com/openai/whisper) d’OpenAI.
