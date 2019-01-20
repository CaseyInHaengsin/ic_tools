from flask import Flask
from config import Config
from flask_login import LoginManager
from app.database import global_init as mongo_setup


app = Flask(__name__)
app.config.from_object(Config)
mongo_setup()
login = LoginManager(app)


from app import routes



