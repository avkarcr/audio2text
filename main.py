import os
import sys
import whisper
import argparse
import textwrap

from config import UI_LANG, translations, help_ui
from utils import (
    check_args,
    print_supported_languages,
    choose_model_by_ram,
    find_audio_file,
    print_summary,
)


def main():

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--help", action="store_true", help="Show list of supported languages and exit.")
    parser.add_argument("--quiet", action="store_true", help="Quiet mode (without welcome screen).")
    parser.add_argument("--file", help="Path to the audio file (default: data/audio.*).")
    parser.add_argument("--model", choices=["tiny", "base", "small", "medium", "large"],
                        help="Whisper model to use (automatically selected by RAM if not specified).")
    parser.add_argument("--lang", default="en",
                        help=f"Spoken language in the audio (use --help for code reference).")
    parser.add_argument("--ui-lang", default="en", help=f"Interface language: {help_ui} (default: en).")

    args = parser.parse_args()

    if args.help:
        print_supported_languages()
        sys.exit(0)

    ui = translations.get(args.ui_lang)
    if not ui:
        print(f"Interface language is not recognized. Options are : {UI_LANG}")
        sys.exit(1)

    check_args(args.help, args.lang)

    if not args.quiet:
        print(textwrap.dedent(ui.manual))

    model_name = args.model or choose_model_by_ram(ui)
    print(ui.loading_model.format(model=model_name))

    audio_path = args.file or find_audio_file(ui)
    if not os.path.isfile(audio_path):
        print(ui.no_file, audio_path)
        sys.exit(1)

    model = whisper.load_model(model_name)

    print(ui.processing.format(file=audio_path, lang=args.lang))
    try:
        result = model.transcribe(audio_path, language=args.lang, fp16=False)
        text = result["text"]
        print_summary(ui, text)
        with open("output.txt", "w", encoding="utf-8") as f:
            f.write(text)
        print(ui.text_saved)
    except Exception as e:
        error = str(e).splitlines()[0]
        print(ui.processing_error.format(error=error))


if __name__ == "__main__":
    main()
