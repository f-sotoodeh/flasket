from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from extensions import db


class User(db.Document, UserMixin):
    username = db.StringField()
    password = db.StringField()
    meta = dict(
        indexes='username'.split(),
    )

    def set_password(self, password):
        self.update(password=generate_password_hash(password, method='sha256'))

    def check_password(self, password):
        return check_password_hash(self.password, password)
    

class Post(db.Document):
    title = db.StringField()
    summary = db.StringField()
    text = db.StringField()
    author = db.StringField()
    datetime = db.DateTimeField()

