from flask import Flask
app = Flask(__name__)

# Create a root route ("/") that responds with "Hello World!"
@app.route('/')
def hello_world():
    return "Hello World!"

# Create a route that responds with "Dojo!"
@app.route('/dojo')
def dojo():
    return "Dojo!"

# Create a route that responds with "Hi" and whatever name is in the URL after /say/
@app.route('/say/<name>')
def say_hi(name):
    if name.isnumeric():
        return "Provided name has to be a string"
    return f"Hi {name.capitalize()}!"

# Create a route that responds with the given word repeated as many times as specified in the URL
@app.route('/repeat/<int:times>/<word>')
def repeat_word(times, word):
    if word.isnumeric():
        return "2nd element in the url should be a number and 3rd element a string"
    else: 
        return word * times

if __name__ == "__main__":
    app.run(debug=True)


