

from mods.utils import _


def model_to_menu(*args):
    menu = []
    for model in args:
        if type(model) != str:
            model = model.__name__
        model = model.lower()
        menu.append(dict(name=model, title=_(model+'s'), href=f'/panel/t/{model}'))
    return menu

user_menu = [
    dict(title=_('profile'), href=f'/panel/u/profile'),
    dict(title=_('logout'), href=f'/panel/u/logout'),
]

