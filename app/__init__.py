from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_login import LoginManager
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = 'banana'
csrf = CSRFProtect(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)


from app import routes, models

@login_manager.user_loader
def load_user(id):
    return models.User.query.get(int(id))
