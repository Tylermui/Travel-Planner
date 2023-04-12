# ---- Workspace setup instructions: ----
# python3 -m venv travel-env
# source travel-env/bin/activate
# pip install flask

# ---- Running the program ----
# source travel-env/bin/activate
# flask --app app run 

from flask import Flask, render_template, redirect, url_for, request, session, g
import sqlite3
app = Flask(__name__)
app.secret_key = 'your_secret_key'

db = sqlite3.connect('my_database.db')
cursor = db.cursor()


class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

users = []
users.append(User(id=1, username='Tyler', password='password'))
users.append(User(id=2, username='Jason', password='secret'))
users.append(User(id=3, username='Thomas', password='somethingsimple'))

# Route to the main page
@app.route('/user/<user_id>/planner')
def home(user_id):
    if not g.user:
        return redirect(url_for('login'))
# find a way to save the content of the page for each user and then render it to the corresponding ID
    # elif g.user:
    #     return redirect(url_for('home', user_id))
    
    # Try to get the html field from the DB
    # if it exists for this user, then return reder_template with body_content=body
    # else just return render_template
    return render_template("index.html") #, body_content="<h1>Current Trip</h1>")

# Route for handling the save page logic
@app.route('/save', methods=['POST'])
def save():
    # body = request.post['body']
    username = session.get('username')
    
    # retrieving the variable from the request
    if request.method == 'POST':
        data = request.get_json()
        body = data['body']
        # # save body as html text to database for userid, need to get the userid
        # cursor.execute("INSERT INTO pages (user_id, html) VALUES (?, ?)", (userid, body))
        # db.commit()
        # db.close()
    
        return 'done'

# always routes to the login page when loading up the app
@app.route('/')
def direct():
    return redirect(url_for('auth.login'))


@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user

if __name__ == "__main__":
    app.run(debug = True)
