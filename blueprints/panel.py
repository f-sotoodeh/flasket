from flask import Blueprint, redirect, render_template, request, url_for, jsonify

from flask_login import current_user, login_required, login_user, logout_user

from mods import forms, menus, models, tables, utils
from mods.utils import _
from settings import APP_TITLE, MENU, TABLE_SIZE

bp = Blueprint('panel', __name__)


def pack(**kw):
    link, family, direction = utils.get_language_settings()
    return dict(
        language_font_link = link,
        language_font_family = family,
        main_menu = menus.model_to_menu(*[getattr(models, i.capitalize()) for i in MENU]),
        user_menu = menus.user_menu,
        site_title = APP_TITLE,
        direction = direction,
        **kw,
    )

@bp.get('/login/')
@bp.get('/login/<message>/')
def login_get(message=''):
    data = pack(
        page_name = _('Login'),
        form = forms.Login(),
        message = _(message, default=''),
    )
    return render_template('panel/login.html', **data)

@bp.post('/login/')
def login_post():
    form = forms.Login(request.form)
    if not request.form or not form.validate():
        return redirect(url_for('panel.login_get', message='invalid_request'))
    try:
        su = models.Super_user.objects.get(username=form.username.data)
        if su.check_password(form.password.data):
            next_page = request.args.get('next')
            login_user(su, bool(form.remember.data))
            return redirect(next_page or url_for('panel.dashboard'))
        else:
            raise Exception()
    except:
        return redirect(url_for('panel.login_get', message='wrong_credentials'))

@bp.get('/u/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('panel.login_get'))

@bp.get('/u/profile/')
@login_required
def profile_get():
    form = forms.Profile(obj=current_user)
    data = pack(
        page_name = _('profile'),
        form = form,
    )
    return render_template('panel/profile.html', **data)

@bp.post('/u/profile/')
@login_required
def profile_post():
    pass

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
    objects = objects.skip((page_number-1)*TABLE_SIZE).limit(TABLE_SIZE)
    table = getattr(tables, model_name.capitalize())(objects)
    data = pack(
        page_name = _(model_name.capitalize()+'s'),
        pages = utils.paginate(objects.count(), TABLE_SIZE, page_number),
        page_number = page_number,
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
    table = getattr(tables, model_name.capitalize())(model.objects.limit(0))
    if request.form and form.validate():
        data = dict()
        for field in form._fields.values():
            if field.name != 'csrf_token':
                data[field.name] = field.data
        if _id == 'new': 
            if table.creatable:
                model(**data).save()
        else:
            model.objects.get(id=_id).update(**data)
    return redirect(url_for('panel.table_get', model_name=model_name))

@bp.delete('/f/<model_name>/<_id>/')
@login_required
def form_delete(model_name, _id):
    """
    """
    form = getattr(forms, model_name.capitalize())
    if success:=form.deletable:
        model = getattr(models, model_name.capitalize())
        model.objects.get(id=_id).delete()
    return jsonify(success=success)

