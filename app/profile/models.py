from app.extensions import *
import datetime, enum
from sqlalchemy.sql import func
from flask import redirect, url_for, request


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    occupation = db.Column(db.String(300))
    street_name = db.Column(db.String(300))
    city = db.Column(db.String(300))
    state_province = db.Column(db.String(300))
    postal_code = db.Column(db.String(12))

    created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, unique=True)
    user = db.relationship('User', back_populates='profile')

    def __str__(self):
        return f"Profile : {self.id}"

    def create_profile(occupation, street_name, city, state_province, current_user):
        new_profile = Profile(occupation=occupation, street_name=street_name, city=city, state_province=state_province, user=current_user)
        try:
            db.session.add(new_profile)
            db.session.commit()
            return None, new_profile
        except Exception as e:
            db.session.rollback()
            return str(e), None
        
    def to_dict(self):
        return {
            'occupation': self.occupation,
            'street_name': self.street_name,
            'city': self.city,
            'state_province': self.state_province,
            'socials':[s.to_dict() for s in profilesocials]
        }


class SocialEnum(enum.Enum):
    github = 'github'
    linkedin = 'linkedin'
    email = 'email'
    phone = 'phone'
    portfolio = 'portfolio'


class ProfileSocial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    social = db.Column(db.Enum(SocialEnum), default=SocialEnum.email, nullable=False)
    social_link = db.Column(db.String(300))

    created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)
    profile = db.relationship('Profile', backref='profilesocials', lazy=True)

    def __str__(self):
        return f"Social : {self.id}"

    def create_instance(social, social_link, profile_instance):
        new_instance = ProfileSocial(social=social, social_link=social_link, profile_instance=profile_instance)
        try:
            db.session.add(new_instance)
            db.session.commit()
            return None, new_instance
        except Exception as e:
            db.session.rollback()
            return str(e), None
        
    def to_dict(self):
        return {
            'social': self.social,
            'social_link': self.social_link
        }
