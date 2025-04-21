from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.resume.models import ExperienceModel
from app.user.decorators import auth_users

@jwt_required()
@auth_users()
def ExperienceModelCreateAPI():
    data = request.get_json()

    job_title = data.get('job_link', None)
    employer = data.get('employer', None)
    location = data.get('location', None)
    start_date = data.get('start_date', None)
    end_date = data.get('end_date', None)
    resumemodel_id = data.get('resumemodel_id', None)

    error, p = ExperienceModel.create_instance(job_title, employer, location, start_date, end_date, resumemodel_id)
    if p:
        return jsonify(p.to_dict()), 201
    return jsonify({'message': f'Error : {error}'}), 401


@jwt_required()
@auth_users()
def ExperienceModelJobDescriptionCreateAPI():
    data = request.get_json()

    id = data.get('id', None)
    new_job_responsibility = data.get('job_responsibility', None)

    try:
        ExperienceModel.create_job_responsibility(id, new_job_responsibility)
        return jsonify({'message':'success'}), 201
    except Exception as e:
        return str(e), None
        return jsonify({'message': f'Error : {str(e)}'}), 404