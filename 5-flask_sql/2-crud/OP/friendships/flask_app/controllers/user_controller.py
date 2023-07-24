from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user_model import User


@app.route("/adduser", methods=['POST'])
def add_user():
    User.create(request.form)
    return redirect("/friendships")
