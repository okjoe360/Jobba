from flask_admin import AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import redirect, url_for
from app.extensions import admin, db
from .models import User

class CustomAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        if not current_user.is_authenticated:
            return redirect(url_for('user.login'))
        return super().index()

class UserAdminView(ModelView):
    #can_delete = False
    page_size = 100

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin()

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('userBP.login', next=request.url))

admin.add_view(UserAdminView(User, db.session))
