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

@bp.get('/f/<model_name>/<_id>/')
def form_get(model_name, _id):
    """
    """
    if _id == 'new':
        form = getattr(forms, model_name.capitalize())()
    else:
        obj = getattr(models, model_name.capitalize()).objects.get(id=_id)
        form = getattr(forms, model_name.capitalize())(obj=obj)
    data = pack(
        page_name = getattr(farsi, model_name.capitalize()),
        form = form,
    )
    return render_template('panel/form.html', **data)

@bp.post('/f/<model_name>/<_id>/')
def form_post(model_name, _id):
    """
    """
    form = getattr(forms, model_name.capitalize())(request.form)
    if request.form and form.validate():
        for field in form._fields.values():
            # field,name
            # field.data
            pass
    return redirect(url_for('panel.table_get', model_name=model_name))

