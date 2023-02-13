from flask import Flask, render_template, request, redirect  # Import Flask to allow us to create our app
from users import Users

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def dashboard():
    return redirect('/users')

@app.route('/users')          # The "@" decorator associates this route with the function immediately following
def all_users():
    result = Users.get_all_users()
    # print(result)
    return render_template("read_all.html", users = result)  # Return the string 'Hello World!' as a response

@app.route('/users/new')
def new_user_form():
    return render_template("create.html")

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

@app.route('/users/show/<int:id>')
def show_one_user(id):
    data = {'id':id}
    one_user = Users.get_user_by_id(data)
    return render_template("read_one.html", user = one_user)

@app.route('/users/edit/<int:id>')
def edit_user(id):

    data = {'id': id}
    one_user = Users.get_user_by_id(data)
    return render_template("edit.html", user = one_user)

@app.route('/users/update', methods=['POST'])
def update():
    Users.update_user(request.form)
    # print(request.form)
    return redirect(f"/users/show/{request.form['id']}")

@app.route('/users/delete/<int:id>')
def delete(id):
    data = {'id': id}
    Users.delete_user(data)
    return redirect('/users')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
