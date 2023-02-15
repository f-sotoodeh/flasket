from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import InputRequired

from mods.utils import _


class Super_user(FlaskForm):
    fname = StringField(_('fname'), validators=[InputRequired()])
    lname = TextAreaField(_('lname'))
    username = StringField(_('username'), validators=[InputRequired()])
    deletable = False


class Login(FlaskForm):
    username = StringField(_('username'))
    password = PasswordField(_('password'))
    remember = BooleanField(_('remember_me'))


class Profile(FlaskForm):
    fname = StringField(_('fname'))
    deletable = False


class Article(FlaskForm):
    title = StringField(_('title'))
    summary = TextAreaField(_('summary'))
    body = TextAreaField(_('body'))
    deletable = True

