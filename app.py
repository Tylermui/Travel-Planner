# ---- Workspace setup instructions: ----
# python3 -m venv travel-env
# source travel-env/bin/activate
# pip install flask

# ---- Running the program ----
# source travel-env/bin/activate
# flask --app app run 

from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

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
@app.route('/home')
def home():
    return render_template("index.html")

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

# Route for handling the logout button
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

# always routes to the login page when loading up the app
@app.route('/')
def direct():
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug = True)
