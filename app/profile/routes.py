from flask import Blueprint
from .controllers import createProfileAPI, createProfileSocialAPI

profileBP = Blueprint('profileBP', __name__)

""" API ROUTES """
profileBP.route("/create", methods = ['POST'])(createProfileAPI)

profileBP.route("/social/create", methods = ['POST'])(createProfileSocialAPI)