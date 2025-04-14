from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user, logout_user
from .models import User

saved_category_list = []

def login():
    if current_user.is_authenticated:
        flash('You are already logged', 'success')
        return redirect(url_for('storeBP.home'))

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        error, new_user = User.login_user(email, password)
        if not error:
            flash('Login successful', 'success')
            return redirect(url_for('storeBP.home'))
        flash("Email or Password Incorrect", 'danger')
    return render_template("login.html", category=saved_category_list)


def register():
    if current_user.is_authenticated:
        flash('You are already logged', 'success')
        return redirect(url_for('storeBP.home'))

    if request.method == 'POST':
        email = request.form.get('email')
        if '@' not in email:
            flash("Email is incorrect", 'danger')
        password = request.form.get('password')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        error, new_user = User.register_user(email, password, first_name, last_name)
        if not error:
            flash('New User Created', 'success')
            return redirect(url_for('userBP.login'))
        flash(error, 'danger')    
    return render_template("register.html", category=saved_category_list)



@login_required
def logout():
    logout_user()
    flash('Logging you out', 'success')
    return redirect(url_for('userBP.login'))


def help_center():
    return render_template("help_center.html", category=saved_category_list)
