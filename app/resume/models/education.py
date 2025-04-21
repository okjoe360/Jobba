from app.extensions import *
import enum

class EducationModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    degree = db.Column(db.String(300))
    school = db.Column(db.String(300))
    field_of_study = db.Column(db.String(300))
    month_year_of_grad = db.Column(db.String(300))
    certificate_link = db.Column(db.String(300))
    is_ongoing = db.Column(db.Boolean, default=False)

    extra_params = db.Column(db.JSON)

    is_active = db.Column(db.Boolean, default=True)
    created = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    updated = db.Column(db.DateTime(timezone=True), onupdate=db.func.now())

    resumemodel_id = db.Column(db.Integer, db.ForeignKey('resume_model.id'), nullable=False)
    resumemodel = db.relationship('ResumeModel', backref='education', lazy=True)

    def __str__(self):
        return f"{self.job_title}"

    def to_dict(self):
        return {
            'id': self.id,
            'degree': self.degree,
            'school': self.school,
            'field_of_study': self.field_of_study,
            'month_year_of_grad': self.month_year_of_grad,
            'certificate_link': self.certificate_link,
            'is_ongoing': self.is_ongoing,
            'is_active': self.is_active
        }