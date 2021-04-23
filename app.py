"""Blogly application."""

from flask import Flask, request, redirect, render_template, flash
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)


@app.route("/users")
def list_users():
    """Show all users."""

    users = User.query.all()
    db.session.commit()
    return render_template("users.html", users=users)


@app.route("/")
def redirect_to_user_list():
    """Redirect to list of users."""

    return redirect("/users")


@app.route("/users/new")
def show_add_user_form():
    """Show an add form for users."""

    
    return render_template("add_user.html")


@app.route("/users/new", methods=["POST"])
def add_user():
    """Process the add form, adding a new user and going back to /users."""

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url']
    image_url = image_url if image_url else None
    db.session.commit()

    if isinstance(first_name, str) and isinstance(last_name, str):
        user = User(first_name=first_name, last_name=last_name, image_url=image_url)
        db.session.add(user)
        db.session.commit()
        return redirect("/users")
    else:
        return render_template("add_user.html")


@app.route(f"/users/<user_id>")
def show_user_info(user_id):
    """Show information about the given user."""

    user = User.query.get_or_404(user_id)
    db.session.commit()
    return render_template("user_info.html", user=user)


@app.route("/users/<user_id>/edit")
def edit_user_info(user_id):
    """Show the edit page for a user."""

    user = User.query.get_or_404(user_id)
    db.session.commit()
    return render_template("edit_user.html", user=user)


@app.route("/users/<user_id>/edit", methods=["POST"])
def edit_user(user_id):
    """Process the edit form, returning the user to the /users page."""

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url']
    image_url = image_url if image_url else None
    user = User.query.get_or_404(user_id)
    user.first_name = first_name
    user.last_name = last_name
    user.image_url = image_url
    db.session.commit()
    return redirect("/users")


@app.route("/users/<user_id>/delete", methods=["GET", "POST"])
def delete_user(user_id):
    """Delete the user."""

    User.query.filter(User.id == user_id).delete()
    db.session.commit()
    return redirect("/users")


    