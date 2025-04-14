from flask_admin import Admin
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
admin = Admin()
bcrypt = Bcrypt()
migrate = Migrate()
cors = CORS()
login_manager = LoginManager()
jwt = JWTManager()