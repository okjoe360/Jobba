from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from ..models import ResumeModel
from app.user.decorators import auth_users

@jwt_required()
@auth_users()
def ResumeCreateAPI():
    data = request.get_json()

    job_title = data.get('job_link', None)
    years_of_experience = data.get('years_of_experience', None)
    file_path = data.get('file_path', None)
    template_name = data.get('template_name', None)

    current_user = get_jwt_identity()

    error, p = ResumeModel.create_instance(job_title, years_of_experience, file_path, template_name, current_user)
    if p:
        return jsonify(p.to_dict()), 201
    return jsonify({'message': f'Error : {error}'}), 401
