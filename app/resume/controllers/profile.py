from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.resume.models import ProfileModel
from app.user.decorators import auth_users

@jwt_required()
@auth_users()
def ProfileCreateAPI():
    data = request.get_json()

    street_name = data.get('street_name', None)
    city = data.get('city', None)
    state_province = data.get('state_province', None)
    postal_code = data.get('postal_code', None)
    phone = data.get('phone', None)
    email = data.get('email', None)
    resumemodel_id = data.get('resumemodel_id', None)

    current_user = get_jwt_identity()

    error, p = ProfileModel.create_instance(street_name, city, state_province, postal_code, phone, email, resumemodel_id)
    if p:
        return jsonify(p.to_dict()), 201
    return jsonify({'message': f'Error : {error}'}), 401



@jwt_required()
@auth_users()
def ProfileSkillCreateAPI():
    data = request.get_json()

    id = data.get('id', None)
    new_skill = data.get('skill', None)

    try:
        ResumeModel.create_skill(id, new_skill)
        return jsonify({'message':'success'}), 201
    except Exception as e:
        return str(e), None
        return jsonify({'message': f'Error : {str(e)}'}), 404


@jwt_required()
@auth_users()
def ProfileSocialCreateAPI():
    data = request.get_json()

    id = data.get('id', None)
    new_social = data.get('social', None)

    try:
        ResumeModel.create_social(id, new_social)
        return jsonify({'message':'success'}), 201
    except Exception as e:
        return str(e), None
        return jsonify({'message': f'Error : {str(e)}'}), 404