from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models.user_model import User


# ============= display route =============
@app.route('/')
def user():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if User.validate_user(request.form):
        hashed_password = bcrypt.generate_password_hash(request.form['password'])
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': hashed_password,
        }
        user_id= User.register(data)
        
        session['user_id']= user_id
        return redirect('/dashboard')
    return redirect('/')

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/login', methods=['POST'])
def login():
    user_from_db = User.get_by_email(request.form)
    if not user_from_db:
        flash("invalid Email / Password", "email")
        return redirect('/')
    if not bcrypt.check_password_hash(user_from_db.password, request.form['password']):
        flash("Invalid Email / Password", "password")
        return redirect('/')
    session['user_name'] = user_from_db.first_name
    return redirect('/dashboard')

@app.route('/recipes/new')
def new_recipe():
    return render_template("new_recipe.html")

@app.route('/user/logout')
def logout():
    session.clear()
    return redirect('/')