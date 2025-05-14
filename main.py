import os
import sys
import glob
import psutil
import whisper
import argparse
import textwrap


def choose_model_by_ram():
    ram_gb = psutil.virtual_memory().total / (1024 ** 3)
    print(f"🔍 ОЗУ: {ram_gb:.1f} GB")
    if ram_gb >= 16:
        return "large"
    elif ram_gb >= 8:
        return "medium"
    elif ram_gb >= 4:
        return "small"
    elif ram_gb >= 2:
        return "base"
    else:
        return "tiny"


def find_audio_file():
    matches = glob.glob("data/audio.*")
    if len(matches) == 0:
        print("❌ Файл audio.* не найден в папке data/\n")
        sys.exit(1)
    elif len(matches) > 1:
        print("❌ Найдено несколько файлов audio.* в папке data/. Удалите лишние.\n")
        for f in matches:
            print(" -", f)
        sys.exit(1)
    return matches[0]


def print_manual():
    print(textwrap.dedent("""
    ─────────────────────────────────────────────────────────────
    🎙️ Распознавание речи из аудиофайлов с помощью Whisper

    📌 Параметры:
      --file     Путь к аудиофайлу (по умолчанию: data/audio.*)
      --model    Модель Whisper: tiny, base, small, medium, large
                 (по умолчанию определяется автоматически по объёму ОЗУ)
      --lang     Язык речи: ru, en, de, fr, es, it, ja, uk и др.
                 (по умолчанию: ru)

    📌 Примеры:
      python main.py
      python main.py --file data/audio.m4a
      python main.py --file data/audio.mp3 --model medium --lang en

    ⚠ Поддерживаемые форматы: wav, mp3, m4a и др.
    💾 Результат сохраняется в output.txt
    ─────────────────────────────────────────────────────────────
    """))


def print_summary(text, max_lines=5, tail_lines=2):
    lines = text.strip().splitlines()
    total = len(lines)
    if total <= max_lines + tail_lines:
        print(text)
    else:
        print("🔹 Начало текста:")
        print("\n".join(lines[:max_lines]))
        print("...\n🔹 Конец текста:")
        print("\n".join(lines[-tail_lines:]))


def main():
    print_manual()

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--file", help="Путь к аудиофайлу (по умолчанию: data/audio.*)")
    parser.add_argument("--model", choices=["tiny", "base", "small", "medium", "large"], help="Модель Whisper")
    parser.add_argument("--lang", default="ru", help="Язык речи (например: ru, en, de, fr, es, it, ja, uk)")

    args = parser.parse_args()

    audio_path = args.file or find_audio_file()
    model_name = args.model or choose_model_by_ram()
    language = args.lang

    if not os.path.isfile(audio_path):
        print(f"❌ Файл не найден: {audio_path}")
        sys.exit(1)

    print(f"📦 Загружается модель: {model_name}")
    model = whisper.load_model(model_name)

    print(f"🎧 Распознаётся: {audio_path} (язык: {language})")
    result = model.transcribe(audio_path, language=language, fp16=False)

    text = result["text"]

    print("\n📝 Распознанный текст (обзор):")
    print_summary(text)

    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(text)

    print("\n💾 Полный текст сохранён в output.txt\n")


if __name__ == "__main__":
    main()
