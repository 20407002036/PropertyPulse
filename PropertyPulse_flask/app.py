#!/usr/bin/python3
from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, logout_user, login_required, current_user
from models.user import User
from models.property import Property
from models.reviews import Review
from flask_migrate import Migrate
from models.db_storage import DBStorage
from flask import session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

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
        print(new_user)
        new_user.save()
        flash('User created successfully!', 'success')
        return redirect('/login')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username)
        user = DBStorage.authenticate_user(DBStorage(), username, password)
        if user:
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect('/dashboard')
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')


@app.route('/dashboard')
@login_required
def dashboard():
    db_storage = DBStorage()
    properties = db_storage.all_properties()

    return render_template('dashboard.html', properties=properties)

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')

@app.route('/profile')
@login_required
def profile():
    user_id = current_user.id
    username = current_user.username
    email = current_user.email
    
    return render_template('profile.html', user_id=user_id, username=username, email=email)

@app.route('/create_property', methods=['GET', 'POST'])
def create_property():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        description = request.form['description']
        rent_price = request.form['rent_price']
        num_bedrooms = request.form['num_bedrooms']
        num_bathrooms = request.form['num_bathrooms']
        size_sqft = request.form['size_sqft']
        amenities = request.form['amenities']
        availability_status = request.form['availability_status']
        contact_email = request.form['contact_email']
        # Get the user_id from the user in session
        username = session.get('username')

        print(f'This is the username {username}')

        new_property = Property(name=name,
                                address=address,
                                description=description,
                                rent_price=rent_price,
                                num_bedrooms=num_bedrooms,
                                num_bathrooms=num_bathrooms,
                                size_sqft=size_sqft,
                                amenities=amenities,
                                availability_status=availability_status,
                                user_id= current_user.id,
                                contact_email=contact_email
                                )

        new_property.save()
        # db_storage = DBStorage()
        # DBStorage.new(DBStorage(), new_property)
        # db_storage.save()
    

        print(new_property.to_dict())
        if new_property:
            return redirect('/profile')
        else:
            flash('Error creating the property')
    return render_template('create_property.html')

@app.route('/review', methods=['POST', 'GET'])
@login_required
def test():
    if request.method == 'POST':
        rental = request.form['rental']
        review = request.form['review']

        new_review = Review(rental=rental,
                            reviewTxt=review
                            )

        new_review.save()

        print(new_review.to_dict())
        print(rental)

    return render_template('review.html')


if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)
