from flask import Flask, redirect, request, flash, send_from_directory
from .extensions import *
from .config import *
from .user.admin import CustomAdminIndexView
from .extensions import *
from .user.models import User
from .user.routes import userBP

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)
    admin.init_app(app)#, name='Admin', template_mode='bootstrap3', index_view=CustomAdminIndexView())
    bcrypt.init_app(app)
    cors.init_app(app, supports_credentials=True, resources={r"/api/*": {"origins": "*"}})
    login_manager.init_app(app)
    jwt.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    @login_manager.unauthorized_handler
    def unauthorized_callback():
        flash("Login to continue", "danger")
        return redirect('/login?next=' + request.path)

    app.register_blueprint(userBP, url_prefix='/user')

    with app.app_context():
        db.create_all()

    return app