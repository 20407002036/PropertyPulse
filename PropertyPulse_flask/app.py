#!/usr/bin/python3

from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, logout_user, login_required
# from models.base_model import BaseModel, Base
from models.user import User
from models.db_storage import DBStorage

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:10229101151@localhost:3306/flask_property_pulse'

db = SQLAlchemy(app)

# User Model
# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), unique=True, nullable=False)
#     password = db.Column(db.String(100), nullable=False)

# Flask-Login Configuration
login_manager = LoginManager(app)



@login_manager.user_loader
def load_user(user_id):
    return DBStorage.get(DBStorage(), User, user_id)


# Routes
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        new_user = User(username=username, email=email, password=password)
        new_user.save()
        flash('User created successfully!', 'success')
        return redirect('/login')
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = DBStorage.authenticate_user(DBStorage(), username, password)

        # ObjUser = User(username, password)

        if user:
            # user.is_active = True
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect('/dashboard')
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')


@app.route('/dashboard')
@login_required
def dashboard():
    context = {
        'user': User.username
    }
    return render_template('dashboard.html', **context)


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/create_property')
def create_property():
    return render_template('create_property.html')


if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)
