from app.extensions import *
import datetime, enum
from sqlalchemy.sql import func
from flask import redirect, url_for, request
from .services import *
from keybert import KeyBERT
#from app.services import ChatGPTClass, gemini_gpt

class JobStatusEnum(enum.Enum):
    created = 'created'
    applied = 'applied'
    interviewed = 'interviewed'
    employed = 'employed'
    rejected = 'rejected'


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(300))
    job_title = db.Column(db.String(300))
    job_link = db.Column(db.String(300))
    job_description = db.Column(db.Text)
    keywords = db.Column(db.JSON)

    status = db.Column(db.Enum(JobStatusEnum), default=JobStatusEnum.created, nullable=False)

    created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='jobs', lazy=True)

    def __str__(self):
        return f"Job : {self.job_title}"

    def create_instance(company, job_title, job_link, job_description, current_user):
        keywords = Job.extract_key_words(job_description)
        #keywords = ChatGPTClass().extract_keywords(job_description)
        #keywords = gemini_gpt(job_description)
        print("keywords =============================================== ", keywords)
        new_instance = Job(company=company, job_title=job_title, job_link=job_link, job_description=job_description, keywords=keywords, user_id=current_user)
        try:
            db.session.add(new_instance)
            db.session.commit()
            return None, new_instance
        except Exception as e:
            db.session.rollback()
            return str(e), None

    def extract_key_words(text):
        ### pip install keybert
        kw_model = KeyBERT()
        keywords = kw_model.extract_keywords(text)
        return keywords
        
    def to_dict(self):
        return {
            'company': self.company,
            'job_title': self.job_title,
            'job_link': self.job_link,
            'job_description': self.job_description,
            'keywords': self.keywords,
            'status': self.status.value,
            'created': self.created
        }

