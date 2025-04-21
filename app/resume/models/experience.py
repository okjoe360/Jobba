from app.extensions import *
import enum

class ExperienceModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(300))
    employer = db.Column(db.String(300))
    location = db.Column(db.String(300))

    start_date = db.Column(db.DateTime(timezone=True))
    end_date = db.Column(db.DateTime(timezone=True))
    is_ongoing = db.Column(db.Boolean, default=False)

    ### JOB DESCRIPTIONS OR RESPONSIBLE ==================================================================================
    job_responsibility = db.Column(db.JSON)

    extra_params = db.Column(db.JSON)

    is_active = db.Column(db.Boolean, default=True)
    created = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    updated = db.Column(db.DateTime(timezone=True), onupdate=db.func.now())

    resumemodel_id = db.Column(db.Integer, db.ForeignKey('resume_model.id'), nullable=False)
    resumemodel = db.relationship('ResumeModel', backref='experience', lazy=True)

    def __str__(self):
        return f"{self.job_title}"

    def create_instance(job_title, employer, location, start_date, end_date, resumemodel_id):
        new_instance = ProfileModel(job_title=job_title, employer=employer, location=location, start_date=start_date, end_date=end_date, resumemodel_id=resumemodel_id)
        try:
            db.session.add(new_instance)
            db.session.commit()
            return None, new_instance
        except Exception as e:
            db.session.rollback()
            return str(e), None

    def create_job_responsibility(id, new_job_responsibility):
        search_instance = ExperienceModel.query.get_or_404(id)
        search_instance.job_responsibility = [new_job_responsibility] + search_instance.job_responsibility
        db.session.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'job_title': self.job_title,
            'employer': self.employer,
            'location': self.location,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'is_ongoing': self.is_ongoing,
            'job_responsibility': self.job_responsibility,
            'is_active': self.is_active
        }