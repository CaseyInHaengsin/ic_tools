from flask import Flask
from config import Config
from flask_login import LoginManager
from app.database import global_init as mongo_setup
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config.from_object(Config)
mongo_setup()
login = LoginManager(app)
bootstrap = Bootstrap(app)

from app import routes



