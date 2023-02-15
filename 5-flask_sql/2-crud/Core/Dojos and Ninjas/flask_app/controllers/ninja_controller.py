from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja

@app.route('/ninjas')
def new_ninja():
    dojos = Dojo.get_all_dojos()
    return render_template("ninjas.html", dojos = dojos)

@app.route('/add_ninja', methods=['post'])
def add_ninja():
    Ninja.add_ninja(request.form)
    print(request.form)
    return redirect("/")