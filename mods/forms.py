from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import InputRequired

class User(FlaskForm):
    fname = StringField('نام', validators=[InputRequired()])
    lname = TextAreaField('فامیل')
