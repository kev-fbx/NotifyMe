from flask import Blueprint, request, render_template, redirect, url_for
from werkzeug.security import generate_password_hash

from utils.db_util import insert_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
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


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')