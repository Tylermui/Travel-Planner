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
    page = None
    try:
        page = Page.query.filter_by(user_id=current_user.id).order_by(Page.id.desc()).first()
        temp = page.data
        if temp:
            body_content = temp
        return render_template("index.html", user=current_user, body_content=body_content, lat_content=page.lat, lng_content=page.lng, is_home=True)
    except:
        pass
    return render_template("index.html", user=current_user, body_content=body_content, lat_content=40.7128, lng_content=-74.0060, is_home=True)

# Route for handling the save page logic
@views.route('/save', methods=['POST'])
def save():
    # retrieving the variable from the request
    if request.method == 'POST':
        data = request.get_json() # Extract the JSON data from the request body
        body = data['body'] # Extract the 'body' property from the JSON data
        lat = data['lat'] # Extract the 'lat' property from the JSON data
        lng = data['lng'] # Extract the 'lng' property from the JSON data
        new_page = Page(data=body, user_id=current_user.id, lat=lat, lng=lng)
        db.session.add(new_page) #adding the page to the database 
        db.session.commit()
        flash('Save complete!', category='success')
    
    return render_template("index.html", user=current_user, is_home=True)
