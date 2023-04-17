from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user
auth = Blueprint('auth', __name__)


# Route for handling the login page logic
@auth.route('/login', methods=['GET', 'POST'])
def login():
    # if request.method == 'POST':
    #     session.pop('user_id', None)
    #     username = request.form['username']
    #     password = request.form['password']
        # validate the username and password here
        # session['username'] = username
        # inserting username and password into users table
        # cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        # db.commit()
        # db.close()
    #     user = [x for x in users if x.username == username][0]
    #     if user and user.password == password:
    #         session['user_id'] = user.id
    #         return redirect(url_for('home', user_id = user.id))
    #     return redirect(url_for('save'))
    # return render_template('login.html')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        # setting the user to the first part of their email
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
    return render_template("login.html", user=current_user)


# Route for handling the logout anchor
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
    
# Route to handle signing up
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        # if statements if the sign-up was not valid
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign-up.html", user=current_user)