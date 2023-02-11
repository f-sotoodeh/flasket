from mods import langs
from settings import LANGUAGE


def get_language():
    return LANGUAGE

def get_language_settings():
    lang = get_language()
    link = langs.FONT_LINKS.get(lang, '')
    family = langs.FONT_FAMILIES.get(lang, '')
    direction =  'rtl' if lang in langs.RTL_LANGUAGES else 'ltr'
    return link, family, direction

def _(text):
    lang = getattr(langs, get_language())
    return getattr(lang, text.lower(), text)

