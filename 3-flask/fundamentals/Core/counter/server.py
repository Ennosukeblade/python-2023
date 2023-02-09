# Import Flask to allow us to create our app
from flask import Flask, render_template, session, redirect
# Create a new instance of the Flask class called "app"
app = Flask(__name__)
app.secret_key = 'You have to be quite'


# The "@" decorator associates this route with the function immediately following
@app.route('/')
def visit():
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 1
    # Return the string 'Hello World!' as a response
    return render_template("index.html", counter=session['visits'])


@app.route('/destroy_session')
def destroy_session():
    session.clear()		# clears all keys
    # session.pop('visits')		# clears a specific key
    return redirect('/')


@app.route('/add_2')
def add_two():
    session['visits'] += 1
    return redirect('/')


@app.route('/reset_session')
def reset_session():
    return redirect('/')


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
