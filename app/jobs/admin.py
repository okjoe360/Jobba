from app.extensions import admin, db
from .models import Profile, ProfileSocial
from app.user.admin import UserAdminView


admin.add_view(UserAdminView(Profile, db.session))
admin.add_view(UserAdminView(ProfileSocial, db.session))
