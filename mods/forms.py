from flask_wtf import FlaskForm
from wt_forms import *


class Post(FlaskForm):
    title = StringField()
    summary = TextAreaField()
    text = TextAreaField()
