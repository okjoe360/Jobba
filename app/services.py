from .extensions import *

def initializer_service(app):
    db.init_app(app)
    migrate.init_app(app, db)
    admin.init_app(app)#, name='Admin', template_mode='bootstrap3', index_view=CustomAdminIndexView())
    bcrypt.init_app(app)
    cors.init_app(app, supports_credentials=True, resources={r"/api/*": {"origins": "*"}})
    login_manager.init_app(app)
    jwt.init_app(app)
