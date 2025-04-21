from app.extensions import *
import enum

class CertificationModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300))
    school = db.Column(db.String(300))
    month_year_of_grad = db.Column(db.String(300))
    certificate_link = db.Column(db.String(300))

    extra_params = db.Column(db.JSON)

    is_active = db.Column(db.Boolean, default=True)
    created = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    updated = db.Column(db.DateTime(timezone=True), onupdate=db.func.now())

    resumemodel_id = db.Column(db.Integer, db.ForeignKey('resume_model.id'), nullable=False)
    resumemodel = db.relationship('ResumeModel', backref='certification', lazy=True)

    def __str__(self):
        return f"{self.job_title}"

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'school': self.school,
            'month_year_of_grad': self.month_year_of_grad,
            'certificate_link': self.certificate_link,
            'is_active': self.is_active
        }