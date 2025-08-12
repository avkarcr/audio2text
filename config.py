from translations import (
    ENMessages, DEMessages, FRMessages, ESMessages, RUMessages,
    ITMessages, PTMessages, KOMessages, JAMessages, ZHMessages,
)
UI_LANG = ["en", "ru", "de", "fr", "es", "it", "pt", "ko", "ja", "zh"]

translations = {
    'en': ENMessages(),
    'de': DEMessages(),
    'fr': FRMessages(),
    'es': ESMessages(),
    'it': ITMessages(),
    'pt': PTMessages(),
    'ru': RUMessages(),
    'ko': KOMessages(),
    'ja': JAMessages(),
    'zh': ZHMessages(),
}

help_ui = ', '.join(translations.keys())
