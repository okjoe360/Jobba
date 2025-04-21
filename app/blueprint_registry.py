from .user.routes import userBP

def register_blueprint(app):
    app.register_blueprint(userBP, url_prefix='/user')
