from flask import Flask
from config import Config
from flask_login import LoginManager
from app.models import db, User
from flask_migrate import Migrate
from flask_moment import Moment

app = Flask(__name__)
app.config.from_object(Config)

login_manager = LoginManager()

login_manager.init_app(app)
db.init_app(app)
migrate = Migrate(app, db)
moment = Moment(app)

# login_manager settings
login_manager.login_view = 'auth.login'
login_manager.login_message = 'You must log in to view this page'
login_manager.login_message_category = 'warning'

# importing blueprints
from app.blueprints.auth import auth
from app.blueprints.main import main
from app.blueprints.posts import posts

# registering blueprints
app.register_blueprint(auth)
app.register_blueprint(main)
app.register_blueprint(posts)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)