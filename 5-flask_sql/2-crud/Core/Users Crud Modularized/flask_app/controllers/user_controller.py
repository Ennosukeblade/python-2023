from flask_app import app
from flask import render_template, request, redirect

from flask_app.models.user_model import Users


# ======== display route : redirect to all users page ======== #
@app.route('/')
def dashboard():
    return redirect('/users')

# ======== display route : all users page ======== #
@app.route('/users')          # The "@" decorator associates this route with the function immediately following
def all_users():
    result = Users.get_all_users()
    return render_template("read_all.html", users = result)  # Return the string 'Hello World!' as a response

# ======== display route : new user page ======== #
@app.route('/users/new')
def new_user_form():
    return render_template("create.html")

# ======== action route : INSERT ======== #
@app.route('/adduser', methods=['POST'])
def add_user():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }
    Users.add_user(data)
    # print(Users.add_user(data)) # trigger the query another time, to avoid
    return redirect("/users")

# ======== display route : one user ======== #
@app.route('/users/show/<int:id>')
def show_one_user(id):
    data = {'id':id}
    one_user = Users.get_user_by_id(data)
    return render_template("read_one.html", user = one_user)

# ======== display route : edit page ======== #
@app.route('/users/edit/<int:id>')
def edit_user(id):

    data = {'id': id}
    one_user = Users.get_user_by_id(data)
    return render_template("edit.html", user = one_user)

# ======== action route : UPDATE ======== #
@app.route('/users/update', methods=['POST'])
def update():
    Users.update_user(request.form)
    # print(request.form)
    return redirect(f"/users/show/{request.form['id']}")

# ======== action route : DELETE ======== #
@app.route('/users/delete/<int:id>')
def delete(id):
    data = {'id': id}
    Users.delete_user(data)
    return redirect('/users')
