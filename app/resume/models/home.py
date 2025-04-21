from app.extensions import *
import datetime, enum


class ExperienceEnum(enum.Enum):
    entry = 'entry'
    mid = 'mid'
    senior = 'senior'
    advance = 'advance'
    management = 'management'


class TemplateEnum(enum.Enum):
    basic = 'basic'


class ResumeModel(db.Model):
    __tablename__ = 'resume_model'
    id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(300), nullable=False)
    years_of_experience = db.Column(db.Enum(ExperienceEnum), default=ExperienceEnum.entry, nullable=False)
    file_path = db.Column(db.String(300), nullable=True)
    template_name = db.Column(db.Enum(TemplateEnum), default=TemplateEnum.basic, nullable=False)
    keywords = db.Column(db.JSON)

    is_active = db.Column(db.Boolean, default=True)
    created = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    updated = db.Column(db.DateTime(timezone=True), onupdate=db.func.now())

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='resume', lazy=True)

    def __str__(self):
        return f"{self.job_title}"

    def create_instance(job_title, years_of_experience, file_path, template_name, current_user):
        new_instance = ResumeModel(job_title=job_title, years_of_experience=years_of_experience, file_path=file_path, template_name=template_name, user_id=current_user)
        try:
            db.session.add(new_instance)
            db.session.commit()
            return None, new_instance
        except Exception as e:
            db.session.rollback()
            return str(e), None

    def to_dict(self):
        return {
            'id': self.id,
            'job_title': self.job_title,
            'years_of_experience': self.years_of_experience,
            'file_path': self.file_path,
            'template': self.template.value,
            'keywords': self.keywords,
            'is_active': self.is_active,
            'profile': self.profile.to_dict() if self.profile else None,
            'experiences': [p.to_dict() for p in self.experience],
            'educations': [p.to_dict() for p in self.education],
            'certifications': [p.to_dict() for p in self.certification],
            'projects': [p.to_dict() for p in self.projects],

        }