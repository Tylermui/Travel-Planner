from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Page
from . import db
import json

views = Blueprint('views', __name__)

# Route to the main page
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
# find a way to save the content of the page for each user and then render it to the corresponding ID
    body_content= ''
    try:
        temp = Page.query.filter_by(user_id=current_user.id).order_by(Page.id.desc()).first().data
        if temp:
            body_content = temp
    except:
        pass        
    return render_template("index.html", user=current_user, body_content=body_content)

# Route for handling the save page logic
@views.route('/save', methods=['POST'])
def save():
    # retrieving the variable from the request
    if request.method == 'POST':
        body = request.data.decode('utf-8')
        new_page = Page(data=body, user_id=current_user.id)
        db.session.add(new_page) #adding the page to the database 
        db.session.commit()
        flash('Save complete!', category='success')
    
    return render_template("index.html", user=current_user)
