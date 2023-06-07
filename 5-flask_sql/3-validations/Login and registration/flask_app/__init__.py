from flask import Flask

app = Flask(__name__)
app.secret_key = "adamcheater"

DB = "belt_demo_recipe"