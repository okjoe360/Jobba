from app.extensions import *
import enum
from .home import ResumeModel

class ProfileModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    street_name = db.Column(db.String(300))
    city = db.Column(db.String(300))
    state_province = db.Column(db.String(300))
    postal_code = db.Column(db.String(12))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(100))

    ### SKILLS ==================================================================================
    skills = db.Column(db.JSON)

    ### SOCIALS ==================================================================================
    socials = db.Column(db.JSON)

    extra_params = db.Column(db.JSON)

    is_active = db.Column(db.Boolean, default=True)
    created = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    updated = db.Column(db.DateTime(timezone=True), onupdate=db.func.now())

    resumemodel_id = db.Column(db.Integer, db.ForeignKey('resume_model.id'), nullable=False)
    resumemodel = db.relationship('ResumeModel', backref='profile', lazy=True)

    def __str__(self):
        return f"{self.id}"

    def create_instance(street_name, city, state_province, postal_code, phone, email, resumemodel_id):
        new_instance = ProfileModel(street_name=street_name, city=city, state_province=state_province, postal_code=postal_code, phone=phone, email=email, resumemodel_id=resumemodel_id)
        try:
            db.session.add(new_instance)
            db.session.commit()
            return None, new_instance
        except Exception as e:
            db.session.rollback()
            return str(e), None

    def create_skill(id, new_skill):
        search_instance = ProfileModel.query.get_or_404(resumemodel_id)
        search_instance.skills = [new_skill] + search_instance.skills
        db.session.commit()

    def create_social(id, new_social):
        search_instance = ProfileModel.query.get_or_404(resumemodel_id)
        search_instance.skills = [new_social] + search_instance.socials
        db.session.commit()

    def to_dict(self):
        return {
            'street_name': self.street_name,
            'city': self.city,
            'state_province': self.state_province,
            'postal_code': self.postal_code,
            'phone': self.phone,
            'email': self.email,
            'skills': self.skills,
            'socials': self.socials
        }

class PlatformEnum(enum.Enum):
    linkedin = 'linkedin'
    github = 'github'
    facebook = 'facebook'
    instagram = 'instagram'
    tiktok = 'tiktok'

"""
SOCIALS FORMAT

{
    'id': <<uuid>>,
    'platform': '',
    'handle': '',
    'is_active': True,
    'datetime_created': db.func.now(),
}
"""