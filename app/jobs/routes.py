from flask import Blueprint
from .controllers import jobCreateAPI

jobsBP = Blueprint('jobsBP', __name__)

""" API ROUTES """
jobsBP.route("/create", methods = ['POST'])(jobCreateAPI)