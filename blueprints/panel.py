from flask import Blueprint, redirect, render_template, request, url_for, jsonify

from flask_login import current_user, login_required, login_user, logout_user

from mods import forms, menus, models, tables, utils
from mods.utils import _
from settings import APP_TITLE

bp = Blueprint('panel', __name__)
PAGE_SIZE = 15

def pack(**kw):
    link, family, direction = utils.get_language_settings()
    return dict(
        language_font_link = link,
        language_font_family = family,
        main_menu = menus.model_to_menu(models.Article, models.Super_user),
        user_menu = menus.user_menu,
        site_title = APP_TITLE,
        direction = direction,
        **kw,
    )

def paginate(count, page_size, page_number):
    return []


@bp.get('/login/')
def login_get(message=''):
    data = pack(
        page_name = _('Login'),
        form = forms.Login(),
        message = message,
    )
    return render_template('panel/login.html', **data)

@bp.post('/login/')
def login_post():
    form = forms.Login(request.form)
    if not request.form or not form.validate():
        raise Exception('aaaaaa')            ############################
    try:
        su = models.Super_user.objects.get(username=form.username.data)
        if su.check_password(form.password.data):
            next_page = request.args.get('next')
            login_user(su) #, bool(form.data.remember, False)) ######
            return redirect(next_page or url_for('panel.dashboard'))
        else:
            raise Exception('bbbbbbbbbbbb')          ##################
    except Exception as e:
        return redirect(url_for('panel.login_get', message=str(e)))

@bp.get('/u/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('panel.login_get'))

@bp.get('/')
@login_required
def dashboard():
    data = pack()
    return render_template('panel/dashboard.html', **data)

@bp.get('/t/<model_name>/')
@bp.get('/t/<model_name>/<page_number>/')
@login_required
def table_get(model_name, page_number=1):
    """
    """
    page_number = int(page_number)
    model = getattr(models, model_name.capitalize())
    objects = model.objects
    objects = objects.skip((page_number-1)*PAGE_SIZE).limit(PAGE_SIZE)
    table = getattr(tables, model_name.capitalize())(objects)
    data = pack(
        page_name = _(model_name.capitalize()+'s'),
        pages = paginate(objects.count(), PAGE_SIZE, page_number),
        current_page = page_number,
        model_name = model_name,
        table = table,
    )
    return render_template('panel/table.html', **data)

@bp.get('/f/<model_name>/<_id>/')
@login_required
def form_get(model_name, _id):
    """
    """
    if _id == 'new':
        form = getattr(forms, model_name.capitalize())()
    else:
        obj = getattr(models, model_name.capitalize()).objects.get(id=_id)
        form = getattr(forms, model_name.capitalize())(obj=obj)
    data = pack(
        page_name = _(model_name.capitalize()),
        model_name = model_name,
        form = form,
        _id = _id,
    )
    return render_template('panel/form.html', **data)

@bp.post('/f/<model_name>/<_id>/')
@login_required
def form_post(model_name, _id):
    """
    """
    form = getattr(forms, model_name.capitalize())(request.form)
    model = getattr(models, model_name.capitalize())
    if request.form and form.validate():
        data = dict()
        for field in form._fields.values():
            if field.name != 'csrf_token':
                data[field.name] = field.data
        if _id == 'new':
            model(**data).save()
        else:
            model.objects.get(id=_id).update(**data)
    return redirect(url_for('panel.table_get', model_name=model_name))

@bp.delete('/f/<model_name>/<_id>/')
@login_required
def form_delete(model_name, _id):
    """
    """
    model = getattr(models, model_name.capitalize())
    model.objects.get(id=_id).delete()
    return jsonify()

