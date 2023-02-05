from flask import Flask

from extensions import db, login


app = Flask(__name__)
app.config.from_pyfile('settings.py')
db.init_app(app)
login.init_app(app)




