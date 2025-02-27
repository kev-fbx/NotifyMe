from flask import Flask, redirect, render_template, request, url_for
from werkzeug.security import generate_password_hash

from models.db_util import insert_user

app = Flask(__name__)


# app.config['SQLALCHEMY_USER_DB_URI'] = f'postgresql://postgres:7026@localhost:6432/User'

# app.config['SQLALCHEMY_BINDS'] = {
#     'ptv': f'postgresql://postgres:7026@localhost:5432/PTV'
# }

# db = SQLAlchemy(app)

# class Profile(db.Model):
#     __tablename__ = 'profile'

#     user_ID = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String, nullable=False)
#     phone = db.Column(db.String)
#     password_hash = db.Column(db.String, nullable=False)

#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)

#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)


# class Subscription(db.Model):
#     __tablename__ = 'subscription'
#     __bind_key__ = None

#     subscription_ID = db.Column(db.Integer, primary_key=True)
#     user_ID = db.Column(db.Integer, db.ForeignKey('profile.user_ID'), nullable=False)
#     station_ID = db.Column(db.Integer, nullable=False)

# class Station(db.Model):
#     __tablename__ = 'station'
#     __bind_key__ = 'ptv'

#     station_ID = db.Column(db.Integer, primary_key=True)
#     stationName = db.Column(db.String, nullable=False)

# class Departure(db.Model):
#     __tablename__ = 'departure'
#     __bind_key__ = 'ptv'

#     departure_ID = db.Column(db.Integer, primary_key=True)
#     station_ID = db.Column(db.Integer, db.ForeignKey('station.station_ID'), nullable=False)
#     departureTime = db.Column(db.Time, nullable=True)
#     toCity = db.Column(db.Boolean, nullable=True)

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