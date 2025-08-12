# 🌍 Idiomas Disponibles

🇬🇧 [Inglés](README.md) | 🇨🇳 [Chino](README_ZH.md) | 🇪🇸 [Español](README_ES.md) | 🇩🇪 [Alemán](README_DE.md) | 🇫🇷 [Francés](README_FR.md) | 🇮🇹 [Italiano](README_IT.md) | 🇵🇹 [Portugués](README_PT.md) | 🇷🇺 [Ruso](README_RU.md) | 🇰🇷 [Coreano](README_KO.md) | 🇯🇵 [Japonés](README_JA.md)

---
# 🧠 Whisper Reconocimiento de Voz a Texto (Offline)

Un script en Python para el **reconocimiento automático de voz a partir de archivos de audio** usando el modelo [Whisper](https://github.com/openai/whisper).  
Después de la descarga e instalación, la transcripción se realiza **localmente** en tu ordenador sin enviar datos a ningún servidor.

- Reconoce voz en más de 100 idiomas.  
  Para listar los idiomas, ejecuta el script con --help.
- El idioma de la interfaz se puede seleccionar con --ui-lang.  
  Ejecuta el script sin parámetros para ver las opciones disponibles.
- Modelos soportados: tiny, base, small, medium, large.  
  Cuanto más "grande" sea el modelo, mayores serán los requisitos de recursos y mejor la precisión.  
  Si no se proporciona --model, el script selecciona automáticamente un modelo en función de la RAM disponible.
- Proporciona un archivo de audio con --file. Formatos soportados: .wav, .mp3, .m4a, .ogg, etc.  
- Muestra una vista previa corta y guarda el texto completo en output.txt.

**⚠ Importante:**  
En el primer uso de un modelo Whisper seleccionado, se descargará **automáticamente de internet**.  
El tamaño de los modelos es grande: desde ~150MB (tiny) hasta ~3GB (large). Asegúrate de tener una conexión estable y suficiente espacio en disco.

---

## 🖥️ Requisitos del Sistema
- SO: Windows 10/11, Ubuntu 20.04+, macOS 11+  
- RAM: mínimo 4GB (16GB recomendados para large)  
- Espacio en disco: ~6GB libres  
- CPU: x86_64 con soporte AVX (recomendado)

📦 Una vez descargado, el modelo funciona completamente offline.

## ✅ Requisitos
- **Python** 3.10  
- **ffmpeg** (decodificación de audio)  
- **git** (clonado del repositorio)

---

## ⚙️ Instalación

### 🪟 Windows

1. Instalar [Python 3.10](https://www.python.org/downloads/)

2. Instalar **Git** (https://git-scm.com/download/win) — elegir *"Git from the command line"* durante la instalación.

3. Instalar **ffmpeg**: descargar desde https://ffmpeg.org/download.html, descomprimir y añadir `bin/` al `PATH` (o colocar ffmpeg.exe junto al script).

4. Clonar el repositorio:
```bash
git clone https://github.com/avkarcr/audio2text.git
cd audio2text
```

5. Crear y activar un entorno virtual:
```bash
python -m venv venv
venv\Scripts\activate
```

6. Instalar dependencias:
```bash
pip install -r requirements.txt
```

---

### 🐧 Linux (Ubuntu/Debian)

1. Instalar **Python 3.10+**. En Ubuntu 22.04+ viene preinstalado:
```bash
python3 --version
```

2. Instalar **git** y **ffmpeg**:
```bash
sudo apt update
sudo apt install git ffmpeg
```

3. Clonar el repositorio:
```bash
git clone https://github.com/avkarcr/audio2text.git
cd audio2text
```

4. Crear y activar un entorno virtual:
```bash
python3 -m venv venv
source venv/bin/activate
```

5. Instalar dependencias:
```bash
pip install -r requirements.txt
```

---

## 🚀 Uso

1. Coloca audio.mp3 en la carpeta data/.  
2. Ejecuta:
```bash
python main.py
```

📦 El modelo y el archivo se seleccionarán automáticamente.  
En la primera ejecución de un modelo, se descargará automáticamente.

---

## 💡 Ejemplos

Ejecutar con el modelo medium en inglés (predeterminado) con interfaz en inglés (predeterminado):
```bash
python main.py --quiet --file data/audio.mp3 --model medium
```

Ejecutar con audio en coreano e interfaz en coreano:
```bash
python main.py --quiet --file data/audio.mp3 --model medium --lang ko --ui-lang ko
```
---

## 📄 Salida

📝 Vista previa del texto reconocido, transcripción completa guardada en output.txt.

---

## ⚠ Notas
- El modelo large requiere 16+GB de RAM.  
- Para audio largo, se recomienda al menos el modelo medium (o dividir el archivo con ffmpeg).

---

## 📚 Licencia
MIT. Utiliza componentes de [Whisper](https://github.com/openai/whisper) de OpenAI.