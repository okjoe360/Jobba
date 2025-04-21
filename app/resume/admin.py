from app.extensions import admin, db
from app.user.admin import UserAdminView
from resume.models import ResumeModel, ProfileModel, SocialModel, ExperienceModel, EducationModel, CertificationModel, ProjectsModel


admin.add_view(UserAdminView(ResumeModel, db.session))
admin.add_view(UserAdminView(ProfileModel, db.session))
admin.add_view(UserAdminView(SocialModel, db.session))
admin.add_view(UserAdminView(ExperienceModel, db.session))
admin.add_view(UserAdminView(CertificationModel, db.session))
admin.add_view(UserAdminView(ProjectsModel, db.session))
