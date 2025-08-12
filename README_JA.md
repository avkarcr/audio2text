# 🌍 利用可能な言語

🇬🇧 [英語](README.md) | 🇨🇳 [中国語](README_ZH.md) | 🇪🇸 [スペイン語](README_ES.md) | 🇩🇪 [ドイツ語](README_DE.md) | 🇫🇷 [フランス語](README_FR.md) | 🇮🇹 [イタリア語](README_IT.md) | 🇵🇹 [ポルトガル語](README_PT.md) | 🇷🇺 [ロシア語](README_RU.md) | 🇰🇷 [韓国語](README_KO.md) | 🇯🇵 [日本語](README_JA.md)

---
# 🧠 Whisper 音声からテキストへ (オフライン)

[Whisper](https://github.com/openai/whisper) モデルを使用して、音声ファイルから自動的に**音声認識**を行う Python スクリプトです。  
ダウンロードとセットアップ後、文字起こしはデータをサーバーに送信することなく**ローカル**で実行されます。

- 100以上の言語に対応。  
  言語一覧を表示するには、`--help` を付けて実行します。
- インターフェースの言語は `--ui-lang` で指定可能。  
  パラメータなしでスクリプトを実行すると、利用可能なオプションが表示されます。
- 利用可能なモデル: tiny, base, small, medium, large。  
  モデルが「大きい」ほど、必要なリソースは増えますが、精度も向上します。  
  `--model` を指定しない場合、利用可能なRAMに基づき自動でモデルを選択します。
- `--file` で音声ファイルを指定します。対応形式: .wav, .mp3, .m4a, .ogg など。  
- 認識結果の短いプレビューを表示し、全文を output.txt に保存します。

**⚠ 重要:**  
指定したモデルを初めて使用する際には、インターネットから自動的に**ダウンロード**されます。  
モデルのサイズは大きく、tinyで約150MB、largeで約3GBあります。安定したネット接続と十分なディスク容量を確保してください。

---

## 🖥️ システム要件
- OS: Windows 10/11, Ubuntu 20.04+, macOS 11+  
- RAM: 最低4GB（largeでは16GB推奨）  
- ディスク容量: 約6GBの空き  
- CPU: AVX対応のx86_64（推奨）

📦 一度ダウンロードすれば、その後は完全にオフラインで動作します。

## ✅ 必要環境
- **Python** 3.10  
- **ffmpeg**（音声デコード用）  
- **git**（リポジトリのクローン用）

---

## ⚙️ インストール方法

### 🪟 Windows

1. [Python 3.10](https://www.python.org/downloads/) をインストール。

2. **Git** をインストール（https://git-scm.com/download/win）— セットアップ時に *"Git from the command line"* を選択。

3. **ffmpeg** をインストール: https://ffmpeg.org/download.html からダウンロードし、解凍後に `bin/` をPATHに追加（またはスクリプトと同じ場所に ffmpeg.exe を配置）。

4. リポジトリをクローン:
```bash
git clone https://github.com/avkarcr/audio2text.git
cd audio2text
```

5. 仮想環境を作成して有効化:
```bash
python -m venv venv
venv\Scriptsctivate
```

6. 依存関係をインストール:
```bash
pip install -r requirements.txt
```

---

### 🐧 Linux (Ubuntu/Debian)

1. **Python 3.10+** をインストール。Ubuntu 22.04+ では標準でインストール済み:
```bash
python3 --version
```

2. **git** と **ffmpeg** をインストール:
```bash
sudo apt update
sudo apt install git ffmpeg
```

3. リポジトリをクローン:
```bash
git clone https://github.com/avkarcr/audio2text.git
cd audio2text
```

4. 仮想環境を作成して有効化:
```bash
python3 -m venv venv
source venv/bin/activate
```

5. 依存関係をインストール:
```bash
pip install -r requirements.txt
```

---

## 🚀 使い方

1. `data/` フォルダに audio.mp3 を置く。  
2. 実行:
```bash
python main.py
```

📦 モデルとファイルは自動的に選択されます。  
初回実行時、モデルは自動的にダウンロードされます。

---

## 💡 使用例

英語音声（デフォルト）と英語UI（デフォルト）で medium モデルを使用:
```bash
python main.py --quiet --file data/audio.mp3 --model medium
```

韓国語音声と韓国語UIで medium モデルを使用:
```bash
python main.py --quiet --file data/audio.mp3 --model medium --lang ko --ui-lang ko
```

---

## 📄 出力

📝 認識テキストのプレビューを表示し、全文を output.txt に保存します。

---

## ⚠ 注意事項
- large モデルは16GB以上のRAMが必要です。  
- 長時間音声には medium 以上のモデルを推奨（または ffmpeg で分割）。

---

## 📚 ライセンス
MIT。OpenAI [Whisper](https://github.com/openai/whisper) のコンポーネントを使用。
