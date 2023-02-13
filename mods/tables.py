from flask_table import Table, Col

from mods.utils import _, get_language_settings


class Ftable(Table):
    no_items = 'هیچی'
    _, _, direction = get_language_settings()
    alignment = 'right aligned' if direction == 'rtl' else ''
    classes = f'ui selectable {alignment} table'.split()
    @classmethod
    def get_tr_attrs(cls, item):
        return dict(
            onclick = f"window.location='/panel/f/{cls.__name__.lower()}/{item.id}'",
        )


class User(Ftable):
    fname = Col(_('fname'))
    lname = Col(_('lname'))
    username = Col(_('username'))
