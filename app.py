from flask import Flask

from blueprints.panel import bp as panel
from blueprints.public import bp as public
from extensions import db, login


# INITIALIZE APP #
app = Flask(__name__)
app.config.from_pyfile('settings.py')
db.init_app(app)
login.init_app(app)

# REGISTER BLUEPRINTS #
app.register_blueprint(panel, url_prefix='/panel')
app.register_blueprint(public)

# ADD JINJA FILTERS #

# USER LOADER #
@login.user_loader
def load_user():
    pass
