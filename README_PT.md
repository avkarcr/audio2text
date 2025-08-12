# 🌍 Idiomas Disponíveis

🇬🇧 [Inglês](README.md) | 🇨🇳 [Chinês](README_ZH.md) | 🇪🇸 [Espanhol](README_ES.md) | 🇩🇪 [Alemão](README_DE.md) | 🇫🇷 [Francês](README_FR.md) | 🇮🇹 [Italiano](README_IT.md) | 🇵🇹 [Português](README_PT.md) | 🇷🇺 [Russo](README_RU.md) | 🇰🇷 [Coreano](README_KO.md) | 🇯🇵 [Japonês](README_JA.md)

---
# 🧠 Whisper Fala-para-Texto (Offline)

Um script Python para **reconhecimento automático de fala a partir de arquivos de áudio** usando o modelo [Whisper](https://github.com/openai/whisper).  
Após o download e configuração, a transcrição é realizada **localmente** no seu computador sem enviar dados para nenhum servidor.

- Reconhece fala em mais de 100 idiomas.  
  Para listar os idiomas, execute o script com `--help`.
- O idioma da interface pode ser selecionado com `--ui-lang`.  
  Execute o script sem parâmetros para ver as opções disponíveis.
- Modelos suportados: tiny, base, small, medium, large.  
  Quanto “maior” o modelo, maiores os requisitos de recursos — e melhor a precisão.  
  Se `--model` não for especificado, o script seleciona automaticamente um modelo com base na RAM disponível.
- Forneça um arquivo de áudio com `--file`. Formatos suportados: .wav, .mp3, .m4a, .ogg, etc.  
- Exibe uma prévia curta e salva o texto completo em `output.txt`.

**⚠ Importante:**  
Na primeira utilização de um modelo Whisper selecionado, ele será **baixado da internet** automaticamente.  
O tamanho dos modelos varia de ~150MB (tiny) até ~3GB (large). Certifique-se de ter uma conexão estável e espaço suficiente em disco.

---

## 🖥️ Requisitos do Sistema
- SO: Windows 10/11, Ubuntu 20.04+, macOS 11+  
- RAM: mínimo 4GB (16GB recomendados para `large`)  
- Espaço em disco: ~6GB livres  
- CPU: x86_64 com suporte AVX (recomendado)

📦 Após o primeiro download, o modelo funciona totalmente offline.

## ✅ Requisitos
- **Python** 3.10  
- **ffmpeg** (decodificação de áudio)  
- **git** (clonagem do repositório)

---

## ⚙️ Instalação

### 🪟 Windows

1. Instale [Python 3.10](https://www.python.org/downloads/)

2. Instale o **Git** (https://git-scm.com/download/win) — escolha *“Git from the command line”* durante a instalação.

3. Instale o **ffmpeg**: baixe de https://ffmpeg.org/download.html, extraia e adicione `bin/` ao `PATH` (ou coloque `ffmpeg.exe` ao lado do script).

4. Clone o repositório:
```bash
git clone https://github.com/avkarcr/audio2text.git
cd audio2text
```

5. Crie e ative um ambiente virtual:
```bash
python -m venv venv
venv\Scriptsctivate
```

6. Instale as dependências:
```bash
pip install -r requirements.txt
```

---

### 🐧 Linux (Ubuntu/Debian)

1. Instale **Python 3.10+**. No Ubuntu 22.04+ já vem pré-instalado:
```bash
python3 --version
```

2. Instale **git** e **ffmpeg**:
```bash
sudo apt update
sudo apt install git ffmpeg
```

3. Clone o repositório:
```bash
git clone https://github.com/avkarcr/audio2text.git
cd audio2text
```

4. Crie e ative um ambiente virtual:
```bash
python3 -m venv venv
source venv/bin/activate
```

5. Instale as dependências:
```bash
pip install -r requirements.txt
```

---

## 🚀 Uso

1. Coloque o arquivo audio.mp3 na pasta `data/`.  
2. Execute:
```bash
python main.py
```

📦 O modelo e o arquivo serão selecionados automaticamente.  
Na primeira execução de um modelo, ele será baixado automaticamente.

---

## 💡 Exemplos

Executar com o modelo medium em inglês (padrão) e interface em inglês (padrão):
```bash
python main.py --quiet --file data/audio.mp3 --model medium
```
Executar com áudio em coreano e interface em coreano:
```bash
python main.py --quiet --file data/audio.mp3 --model medium --lang ko --ui-lang ko
```
---

## 📄 Saída

📝 Prévia do texto reconhecido, transcrição completa salva em `output.txt`.

---

## ⚠ Observações
- O modelo large requer 16GB ou mais de RAM.  
- Para áudios longos, prefira pelo menos o modelo medium (ou divida o arquivo com ffmpeg).

---

## 📚 Licença
MIT. Usa componentes do [Whisper](https://github.com/openai/whisper) da OpenAI.
