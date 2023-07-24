from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.friendship_model import Friendship
from flask_app.models.friends_model import Friends
from flask_app.models.user_model import User


@app.route("/")
def index():
    return redirect("/friendships")


@app.route("/friendships")
def dashboard():
    friends = Friends.get_friendships()
    users = User.get_all()
    return render_template("index.html", friends=friends, users=users)


@app.route("/makefriend", methods=['POST'])
def make_friend():
    if Friendship.validate_relation(request.form):
        Friendship.create(request.form)
        return redirect("/friendships")
    return redirect("/friendships")
