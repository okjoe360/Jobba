from app.extensions import *
import enum

class ProjectsModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300))
    description = db.Column(db.Text)
    project_link = db.Column(db.String(300))

    extra_params = db.Column(db.JSON)

    is_active = db.Column(db.Boolean, default=True)
    created = db.Column(db.DateTime(timezone=True), server_default=db.func.now())
    updated = db.Column(db.DateTime(timezone=True), onupdate=db.func.now())

    resumemodel_id = db.Column(db.Integer, db.ForeignKey('resume_model.id'), nullable=False)
    resumemodel = db.relationship('ResumeModel', backref='projects', lazy=True)

    def __str__(self):
        return f"{self.job_title}"

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'project_link': self.project_link,
            'is_active': self.is_active
        }