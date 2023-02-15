from persian import convert_en_numbers

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

def _(text, **kw):
    lang_name = get_language()
    lang = getattr(langs, lang_name)
    if str(text).isnumeric(): 
        return dict(
            farsi = convert_en_numbers,
            arabic = convert_en_numbers,
        ).get(lang_name, lambda x: x)(text)
    return getattr(lang, text.lower(), kw.get('default', text.capitalize()))

def paginate(count, page_size, page_number):
    """
    """
    page_count = (count//page_size) + bool(count%page_size)
    left = list(range(1, page_number))[-5:]
    right = list(range(page_number, page_count+1))[:6]
    if len(left) + len(right) > 5:
        left = left[-2:]
        right = right[:3]
    if left and left[0] > 1:
        left = [1, '…'] + left
    if right and right[-1] < page_count:
        right = right + ['…', page_count]
    pages = left + right
    return pages if len(pages) > 1 else []


