from flask import Flask, redirect, render_template, request, url_for
from werkzeug.security import generate_password_hash

from utils.db_util import insert_user

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        phone = request.form['phone']
        pw_hash = request.form['pw_hash']

        if not phone:
            phone = None

        hashed_pw = generate_password_hash(pw_hash)

        insert_user(email, phone, hashed_pw)

        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)