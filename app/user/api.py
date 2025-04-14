from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user, logout_user
from .models import User
from icecream import ic


saved_category_list = []

def loginAPI():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    error, user = User.login_user_for_api(email, password)
    if user:
        return jsonify(user), 200
    return jsonify({'message': 'Invalid credentials'}), 401


def registerAPI():
    if request.method == 'POST':
        data = request.get_json()
        email = data.get('email')
        if '@' not in email:
            return jsonify({'message': 'Invalid email format'}), 401
        password = data.get('password')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        error, new_user = User.register_user(email, password, first_name, last_name)
        if error:
            return jsonify({'message': error}), 401
        return jsonify({'message': 'User created'}), 201


@login_required
def logoutAPI():
    logout_user()
    flash('Logging you out', 'success')
    return redirect(url_for('userBP.login'))