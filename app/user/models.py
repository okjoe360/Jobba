from app.extensions import *
import datetime, enum
from sqlalchemy.sql import func
from flask import redirect, url_for, request
#from flask_bcrypt import generate_password_hash, check_password_hash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, current_user, login_user
from flask_admin.contrib.sqla import ModelView
from .services import genrate_api_keys
from sqlalchemy import event
from flask_jwt_extended import create_access_token

class RolesEnum(enum.Enum):
    user = 'user'
    admin = 'admin'


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False)
    first_name = db.Column(db.String(256))
    last_name = db.Column(db.String(256))
    address = db.Column(db.Text())
    postal_code = db.Column(db.String(12))
    role = db.Column(db.Enum(RolesEnum), default=RolesEnum.user, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    is_admin = db.Column(db.Boolean, default=True)
    created = db.Column(db.DateTime(timezone=True), server_default=func.now())#, default=datetime.datetime.utcnow)
    updated = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


    def login_user(email, password):
        usr = User.query.filter_by(email=email).first()
        if usr and usr.check_password(password) and usr.is_active:
            login_user(usr)
            return None, usr
        return 404, None

    def login_user_for_api(email, password):
        usr = User.query.filter_by(email=email).first()
        if usr and usr.check_password(password) and usr.is_active:
            access_token = create_access_token(identity=usr.id)
            u = usr.to_json()
            u['access_token'] = access_token
            return None, u
        return 404, None

    def register_user(email, password, first_name, last_name):
        new_user = User(email=email, first_name=first_name, last_name=last_name)
        new_user.set_password(password)
        try:
            db.session.add(new_user)
            db.session.commit()
            return None, new_user
        except Exception as e:
            db.session.rollback()
            return str(e), None

    def isAdmin(self):
        if self.role == RolesEnum.admin:
            return True
        return False

    def to_json(self):
        return {
            'id': self.id,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'role': self.role.value,
            'postal_code': self.postal_code,
        }
