from .extensions import *
from .user.models import User
from flask import Flask, redirect, request, flash, send_from_directory

def initializer_service(app):
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
