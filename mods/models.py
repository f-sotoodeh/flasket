from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from extensions import db


class Super_user(db.Document, UserMixin):
    username = db.StringField()
    email = db.StringField()
    fname = db.StringField()
    lname = db.StringField()
    password = db.StringField()
    meta = dict(
        indexes='username'.split(),
    )

    def set_password(self, password):
        self.update(password=generate_password_hash(password, method='sha256'))

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
