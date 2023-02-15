from flask_table import Table, Col

from mods.utils import _, get_language_settings


class Ftable(Table):
    no_items = 'هیچی'
    _, _, direction = get_language_settings()
    alignment = 'right aligned' if direction == 'rtl' else ''
    classes = f'ui selectable {alignment} table'.split()
    creatable = True
    @classmethod
    def get_tr_attrs(cls, item):
        return dict(onclick=f"window.location='/panel/f/{cls.__name__.lower()}/{item.id}'")


class Super_user(Ftable):
    fname = Col(_('fname'))
    lname = Col(_('lname'))
    email = Col(_('email'))
    username = Col(_('username'))
    creatable = False

class Article(Ftable):
    title = Col(_('title'))
