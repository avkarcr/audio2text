# 🌍 可用语言

🇬🇧 [英语](README.md) | 🇨🇳 [中文](README_ZH.md) | 🇪🇸 [西班牙语](README_ES.md) | 🇩🇪 [德语](README_DE.md) | 🇫🇷 [法语](README_FR.md) | 🇮🇹 [意大利语](README_IT.md) | 🇵🇹 [葡萄牙语](README_PT.md) | 🇷🇺 [俄语](README_RU.md) | 🇰🇷 [韩语](README_KO.md) | 🇯🇵 [日语](README_JA.md)

---
# 🧠 Whisper 语音转文字（离线）

这是一个使用 [Whisper](https://github.com/openai/whisper) 模型进行自动**音频文件语音识别**的 Python 脚本。  
下载并设置完成后，转录将在您的计算机上**本地**进行，不会将数据发送到任何服务器。

- 支持识别 100 多种语言的语音。  
  要查看语言列表，请使用 `--help` 参数运行脚本。
- 可以通过 `--ui-lang` 选择界面语言。  
  不带参数运行脚本即可查看可用选项。
- 支持的模型：tiny、base、small、medium、large。  
  模型越大，对计算机资源的要求越高，准确性也越好。  
  如果未提供 `--model` 参数，脚本会根据可用内存自动选择模型。
- 使用 `--file` 提供音频文件。支持的格式：.wav、.mp3、.m4a、.ogg 等。  
- 显示简短的预览，并将完整文本保存到 output.txt。

**⚠ 重要：**  
第一次使用所选 Whisper 模型时，会**自动从互联网下载**。  
模型文件较大——从约 150MB（tiny）到约 3GB（large）。请确保网络连接稳定且有足够磁盘空间。

---

## 🖥️ 系统要求
- 操作系统：Windows 10/11、Ubuntu 20.04+、macOS 11+  
- 内存：至少 4GB（large 推荐 16GB）  
- 磁盘空间：约 6GB 可用空间  
- CPU：支持 AVX 的 x86_64（推荐）

📦 下载一次后，模型即可完全离线使用。

## ✅ 依赖要求
- Python 3.10  
- ffmpeg（音频解码）  
- git（克隆代码库）

---

## ⚙️ 安装步骤

### 🪟 Windows

1. 安装 [Python 3.10](https://www.python.org/downloads/)

2. 安装 [Git](https://git-scm.com/download/win) — 安装时选择 *“Git from the command line”*。

3. 安装 **ffmpeg**：从 https://ffmpeg.org/download.html 下载，解压并将 `bin/` 添加到 PATH（或将 ffmpeg.exe 放到脚本目录）。

4. 克隆代码库：
```bash
git clone https://github.com/avkarcr/audio2text.git
cd audio2text
```

5. 创建并激活虚拟环境：
```bash
python -m venv venv
venv\Scripts\activate
```

6. 安装依赖：
```bash
pip install -r requirements.txt
```

---

### 🐧 Linux (Ubuntu/Debian)

1. 安装 **Python 3.10+**。在 Ubuntu 22.04+ 上已预装：
```bash
python3 --version
```

2. 安装 **git** 和 **ffmpeg**：
```bash
sudo apt update
sudo apt install git ffmpeg
```

3. 克隆代码库：
```bash
git clone https://github.com/avkarcr/audio2text.git
cd audio2text
```

4. 创建并激活虚拟环境：
```bash
python3 -m venv venv
source venv/bin/activate
```

5. 安装依赖：
```bash
pip install -r requirements.txt
```

---

## 🚀 使用方法

1. 将 audio.mp3 放入 data/ 文件夹。  
2. 运行：
```bash
python main.py
```

📦 模型和文件将自动选择。  
首次运行时，所需模型会自动下载。

---

## 💡 示例

使用 medium 模型识别英语（默认），界面语言为英语（默认）：
```bash
python main.py --quiet --file data/audio.mp3 --model medium
```
使用 medium 模型识别韩语音频，界面语言为韩语：
```bash
python main.py --quiet --file data/audio.mp3 --model medium --lang ko --ui-lang ko
```

---

## 📄 输出

📝 显示识别文本的预览，并将完整转录保存到 output.txt。

---

## ⚠ 注意事项
- large 模型需要 16GB 以上内存。  
- 对于较长的音频，建议至少使用 medium 模型（或用 ffmpeg 分割文件）。

---

## 📚 许可协议
MIT。使用了 OpenAI [Whisper](https://github.com/openai/whisper) 的组件。
