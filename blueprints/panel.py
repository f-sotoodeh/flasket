from flask import Blueprint, redirect, render_template, request, url_for

from mods import farsi, forms, models, tables, utils
from settings import SITE_NAME

bp = Blueprint('panel', __name__)
PAGE_SIZE = 15

def pack(**kw):
    return dict(
        menu = dict(),
        site_name = SITE_NAME,
        **kw,
    )

def paginate(count, page_size, page_number):
    return []


@bp.get('/t/<model_name>/')
@bp.get('/t/<model_name>/page_number/')
def table_get(model_name, page_number=1):
    """
    """
    model = getattr(models, model_name.capitalize())
    objects = model.objects
    objects = objects.skip((page_number-1)*PAGE_SIZE).limit(PAGE_SIZE)
    table = getattr(tables, model_name.capitalize())(objects)
    table = tables.User(objects)
    data = pack(
        page_name = getattr(farsi, model_name.capitalize()+'s'),
        table = table,
        pages = paginate(objects.count(), PAGE_SIZE, page_number),
        current_page = page_number,
    )
    return render_template('panel/table.html', **data)