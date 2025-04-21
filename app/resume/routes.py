from flask import Blueprint
from .controllers import *


resumeBP = Blueprint('resumeBP', __name__)

""" API ROUTES """
resumeBP.route("/create", methods = ['POST'])(ResumeCreateAPI)

resumeBP.route("/profile/create", methods = ['POST'])(ProfileCreateAPI)
resumeBP.route("/skill/create", methods = ['POST'])(ProfileSkillCreateAPI)
resumeBP.route("/social/create", methods = ['POST'])(ProfileSocialCreateAPI)
resumeBP.route("/experience/create", methods = ['POST'])(ExperienceModelCreateAPI)
resumeBP.route("/experience/description/create", methods = ['POST'])(ExperienceModelJobDescriptionCreateAPI)