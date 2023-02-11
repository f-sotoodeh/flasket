from flask import Flask

from blueprints.panel import bp as panel
from blueprints.public import bp as public
from extensions import db, login
from mods.utils import _


# INITIALIZE APP #
app = Flask(__name__)
app.config.from_pyfile('settings.py')
db.init_app(app)
login.init_app(app)

# REGISTER BLUEPRINTS #
app.register_blueprint(panel, url_prefix='/panel')
app.register_blueprint(public)

# ADD FILTERS TO JINJA ENVIRONMENT
app.jinja_env.lstrip_blocks = True
app.jinja_env.trim_blocks = True
app.jinja_env.filters.update(
    translate=_,
)

# USER LOADER #
@login.user_loader
def load_user():
    pass
