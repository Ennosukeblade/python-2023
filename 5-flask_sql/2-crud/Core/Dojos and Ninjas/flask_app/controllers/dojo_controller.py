from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.dojo_model import Dojo

@app.route('/')
def dashboard():
    return redirect("/dojos")

# ============= display route =============
@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all_dojos()
    return render_template("dojos.html", dojos = dojos)

# ============= action route =============
@app.route('/add_dojo', methods=['post'])
def add_dojo():
    data = {
        'name': request.form['name']
    }
    Dojo.create_dojo(data)
    return redirect('/')

@app.route('/dojos/<int:id>')
def dojo_ninjas_by_id(id):
    data = {
        'id': id
    }
    infos = Dojo.get_dojo_ninjas(data)
    return render_template("dojo_ninjas.html", infos = infos)

