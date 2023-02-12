from flask import Flask, render_template, request, redirect  # Import Flask to allow us to create our app
from users import Users

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

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

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
