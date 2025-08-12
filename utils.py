import sys
import glob
import psutil

from whisper import tokenizer
from tabulate import tabulate


def print_supported_languages():
    languages = tokenizer.LANGUAGES
    table = sorted([[code, name] for code, name in languages.items()])
    print(tabulate(table, headers=["Code", "Language"], tablefmt="fancy_grid"))


def check_args(help, lang):

    if help:
        print_supported_languages()
        sys.exit(0)

    if lang not in tokenizer.LANGUAGES:
        print("Model language is not recognized")
        print("Critical error. Please check your script arguments.")
        sys.exit(1)


def choose_model_by_ram(ui):
    ram_gb = psutil.virtual_memory().total / (1024 ** 3)
    print(ui.ram_info.format(ram_gb=ram_gb))
    if ram_gb >= 16:
        return "large"
    elif ram_gb >= 8:
        return "medium"
    elif ram_gb >= 4:
        return "small"
    elif ram_gb >= 2:
        return "base"
    return "tiny"


def find_audio_file(ui):
    matches = glob.glob("data/audio.*")
    if len(matches) == 0:
        print(ui.no_file)
        sys.exit(1)
    elif len(matches) > 1:
        print(ui.many_files)
        for f in matches:
            print(" -", f)
        sys.exit(1)
    return matches[0]


def print_summary(ui, text, max_lines=5, tail_lines=2):
    print(ui.summary)
    lines = text.strip().splitlines()
    total = len(lines)
    if total <= max_lines + tail_lines:
        print(text)
    else:
        print(ui.summary_start)
        print("\n".join(lines[:max_lines]))
        print(ui.summary_end)
        print("\n".join(lines[-tail_lines:]))
