from app.database import mongoengine
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login

class User(UserMixin, mongoengine.Document):
    username = mongoengine.StringField(required=True, unique=True)
    password_hash = mongoengine.StringField(min_length=12, max_length=255, required=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


    meta = {
        'db_alias': 'core',
        'collection': 'ic_users'
    }


@login.user_loader
def load_user(id):
    #user_to_return = User.objects().filter(username=id)
    return User.objects().filter(pk=id).first()
