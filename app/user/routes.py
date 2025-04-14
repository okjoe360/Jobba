from flask import Blueprint
from .controllers import login, register, logout, help_center
from . import api

userBP = Blueprint('userBP', __name__)

userBP.route("/login", methods = ['GET', 'POST'])(login)

userBP.route("/register", methods = ['GET', 'POST'])(register)

userBP.route("/logout", methods = ['GET', 'POST'])(logout)

userBP.route("/help", methods = ['GET'])(help_center)

""" API ROUTES """
userBP.route("/api/v1/login", methods = ['POST'])(api.loginAPI)

userBP.route("/api/v1/register", methods = ['POST'])(api.registerAPI)