from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user, logout_user
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from .services import *
#from app.services import ChatGPTClass, gemini_gpt
from .models import Job

@jwt_required()
def jobCreateAPI():
    data = request.get_json()
    company = data.get('company', None)
    job_title = data.get('job_title', None)

    job_link = data.get('job_link', None)
    job_description = data.get('job_description', None)

    current_user = get_jwt_identity()

    if job_link and job_description in [None, 'None', '', ' ']:
        job_description = scrape_with_selenium(job_link)## scrape_job_description(job_link)

    error, p = Job.create_instance(company, job_title, job_link, job_description, current_user)
    if p:
        return jsonify(p.to_dict()), 200
    return jsonify({'message': f'Error : {error}'}), 401

