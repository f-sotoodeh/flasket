from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import InputRequired

from mods.utils import _


class Super_user(FlaskForm):
    fname = StringField(_('fname'), validators=[InputRequired()])
    lname = TextAreaField(_('lname'))
    username = StringField(_('username'), validators=[InputRequired()])
    deletable = False