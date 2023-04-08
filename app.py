# ---- Workspace setup instructions: ----
# python3 -m venv travel-env
# source travel-env/bin/activate
# pip install flask

# ---- Running the program ----
# source travel-env/bin/activate
# flask --app app run 

from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# Route for handling the login page logic
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != 'admin' or request.form['password'] != 'admin':
#             error = 'Invalid Credentials. Please try again.'
#         else:
#             return redirect(url_for('home'))
#     return render_template('login.html', error=error)


if __name__ == "__main__":
    app.run(debug = True)
