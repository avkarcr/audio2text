# 🌍 사용 가능한 언어

🇬🇧 [영어](README.md) | 🇨🇳 [중국어](README_ZH.md) | 🇪🇸 [스페인어](README_ES.md) | 🇩🇪 [독일어](README_DE.md) | 🇫🇷 [프랑스어](README_FR.md) | 🇮🇹 [이탈리아어](README_IT.md) | 🇵🇹 [포르투갈어](README_PT.md) | 🇷🇺 [러시아어](README_RU.md) | 🇰🇷 [한국어](README_KO.md) | 🇯🇵 [일본어](README_JA.md)

---
# 🧠 Whisper 음성-텍스트 변환 (오프라인)

[Whisper](https://github.com/openai/whisper) 모델을 사용하여 **오디오 파일에서 자동으로 음성을 인식**하는 Python 스크립트입니다.  
다운로드 및 설정 후에는 데이터를 서버로 전송하지 않고 **로컬**에서 변환이 수행됩니다.

- 100개 이상의 언어를 인식합니다.  
  언어 목록을 보려면 스크립트를 `--help` 옵션으로 실행하세요.
- `--ui-lang` 옵션으로 인터페이스 언어를 선택할 수 있습니다.  
  매개변수 없이 스크립트를 실행하면 사용 가능한 옵션을 볼 수 있습니다.
- 지원 모델: tiny, base, small, medium, large.  
  모델이 클수록 리소스 요구 사항이 높아지고 정확도가 향상됩니다.  
  `--model`이 지정되지 않으면 사용 가능한 RAM에 따라 자동으로 모델이 선택됩니다.
- `--file` 옵션으로 오디오 파일을 제공하세요. 지원 형식: .wav, .mp3, .m4a, .ogg 등.  
- 짧은 미리보기를 출력하고 전체 텍스트를 output.txt에 저장합니다.

**⚠ 중요:**  
선택한 Whisper 모델을 처음 사용할 때는 인터넷에서 자동으로 다운로드됩니다.  
모델 크기는 약 150MB(tiny)에서 최대 3GB(large)까지 다양합니다. 안정적인 연결과 충분한 디스크 공간을 확보하세요.

---

## 🖥️ 시스템 요구 사항
- OS: Windows 10/11, Ubuntu 20.04+, macOS 11+  
- RAM: 최소 4GB (large 모델은 16GB 권장)  
- 디스크 공간: 약 6GB 이상  
- CPU: AVX를 지원하는 x86_64 (권장)

📦 한 번 다운로드하면 모델은 완전히 오프라인에서 작동합니다.

## ✅ 필수 구성 요소
- **Python** 3.10  
- **ffmpeg** (오디오 디코딩)  
- **git** (저장소 복제)

---

## ⚙️ 설치

### 🪟 Windows

1. [Python 3.10](https://www.python.org/downloads/) 설치

2. [Git](https://git-scm.com/download/win) 설치 — 설치 시 *"Git from the command line"* 선택

3. [ffmpeg](https://ffmpeg.org/download.html) 다운로드, 압축 해제 후 `bin/` 경로를 PATH에 추가 (또는 ffmpeg.exe를 스크립트와 같은 폴더에 두기)

4. 저장소 복제:
```
git clone https://github.com/avkarcr/audio2text.git
cd audio2text
```

5. 가상 환경 생성 및 활성화:
```
python -m venv venv
venv\Scriptsctivate
```

6. 종속성 설치:
```
pip install -r requirements.txt
```

---

### 🐧 Linux (Ubuntu/Debian)

1. **Python 3.10+** 설치. Ubuntu 22.04+에는 기본 설치되어 있음:
```
python3 --version
```

2. **git** 및 **ffmpeg** 설치:
```
sudo apt update
sudo apt install git ffmpeg
```

3. 저장소 복제:
```
git clone https://github.com/avkarcr/audio2text.git
cd audio2text
```

4. 가상 환경 생성 및 활성화:
```
python3 -m venv venv
source venv/bin/activate
```

5. 종속성 설치:
```
pip install -r requirements.txt
```

---

## 🚀 사용 방법

1. `data/` 폴더에 audio.mp3 파일 넣기  
2. 실행:
```
python main.py
```

📦 모델과 파일이 자동으로 선택됩니다.  
해당 모델을 처음 실행할 경우 자동으로 다운로드됩니다.

---

## 💡 예시

영어 오디오와 영어 UI(기본값)로 medium 모델 실행:
```
python main.py --quiet --file data/audio.mp3 --model medium
```

한국어 오디오와 한국어 UI로 실행:
```
python main.py --quiet --file data/audio.mp3 --model medium --lang ko --ui-lang ko
```

---

## 📄 출력

📝 인식된 텍스트 미리보기와 전체 변환 내용은 output.txt에 저장됩니다.

---

## ⚠ 참고 사항
- large 모델은 16GB 이상의 RAM 필요  
- 긴 오디오는 최소 medium 모델 사용 권장 (또는 ffmpeg로 파일 분할)

---

## 📚 라이선스
MIT. OpenAI [Whisper](https://github.com/openai/whisper) 구성 요소 사용
