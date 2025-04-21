from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user, logout_user
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from .models import Profile, ProfileSocial

@jwt_required()
def createProfileAPI():
    data = request.get_json()
    occupation = data.get('occupation', None)
    street_name = data.get('street_name', None)
    city = data.get('city', None)
    state_province = data.get('state_province', None)
    current_user = get_jwt_identity()
    error, p = Profile.create_profile(occupation, street_name, city, state_province, current_user)
    if p:
        return jsonify(p.to_dict()), 200
    return jsonify({'message': f'Error : {error}'}), 401



@jwt_required()
def createProfileSocialAPI():
    data = request.get_json()
    social = data.get('social', None)
    social_link = data.get('social_link', None)
    profile_id = data.get('profile_id', None)
    current_user = get_jwt_identity()
    profile_instance = Profile.query.get_or_404(profile_id)
    error, p = ProfileSocial.create_instance(social, social_link, profile_instance)
    if p:
        return jsonify(p.to_dict()), 200
    return jsonify({'message': f'Error : {error}'}), 401
