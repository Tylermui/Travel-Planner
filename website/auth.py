from flask import Blueprint, render_template, request, flash, redirect, url_for
auth = Blueprint('auth', __name__)


# Route for handling the login page logic
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']
        
        # validate the username and password here
        session['username'] = username
        
        # inserting username and password into users table
        # cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        # db.commit()
        # db.close()
        
        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('home', user_id = user.id))

        return redirect(url_for('save'))

    return render_template('login.html')


# Route for handling the logout button
@auth.route('/logout')
def logout():
    session.pop('user_id', None)
    # new code below this
    # user_id = request.args.get('user_id')
    # updated_html = request.args.get('updated_html')
    # save the updated HTML template to the database using the user_id as a reference
    # db.execute('INSERT INTO pages (user_id, html) VALUES (?, ?)', (user_id, updated_html))
    # db.commit()
    
    return redirect(url_for('login'))