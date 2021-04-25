"""Blogly application."""

from flask import Flask, request, redirect, render_template, flash
from models import db, connect_db, User, Post

app = Flask(__name__)
app.debug = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_RECORD_QUERIES'] = True

connect_db(app)

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)



@app.route("/users")
def list_users():
    """Show all users."""

    users = User.query.all()
    # db.session.commit()
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
    posts = Post.query.filter(Post.user_id == user_id)
    # db.session.commit()
    return render_template("user_info.html", user=user, posts=posts)


@app.route("/users/<user_id>/edit")
def edit_user_info(user_id):
    """Show the edit page for a user."""

    user = User.query.get_or_404(user_id)
    # db.session.commit()
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


@app.route("/users/<user_id>/posts/new")
def show_add_post_form(user_id):
    """Show form to add a post for that user."""

    user = User.query.get_or_404(user_id)
    return render_template("add_post.html", user=user)

@app.route("/users/<user_id>/posts/new", methods=["POST"])
def handle_post_form(user_id):
    """Handle add form; add post and redirect to the user detail page."""
    
    title = request.form['title']
    content = request.form['content']
    db.session.commit()
    
    post = Post(title=title, content=content, user_id=user_id)
    db.session.add(post)
    db.session.commit()
    return redirect(f"/users/{user_id}")


@app.route("/posts/<int:post_id>")
def show_post(post_id):
    """Show a post and buttons to edit and delete the post."""

    post = Post.query.get_or_404(post_id)
    return render_template("post.html", post=post)
    

@app.route("/posts/<post_id>/edit")
def edit_post(post_id):
    """Show form to edit a post, and to cancel (back to user page)."""

    post = Post.query.get_or_404(post_id)
    return render_template("edit_post.html", post=post)

@app.route("/posts/<post_id>/edit", methods=["POST"])
def handle_post_edit(post_id):
    """Handle editing of a post. Redirect back to the post view."""

    title = request.form['title']
    content = request.form['content']
    post = Post.query.get_or_404(post_id)
    post.title = title
    post.content = content
    db.session.commit()
    return redirect(f"/posts/{post_id}")


@app.route("/posts/<int:post_id>/delete", methods=["GET", "POST"])
def delete_post(post_id):
    """Delete the post."""

    post = Post.query.get_or_404(post_id)
    Post.query.filter(Post.id == post_id).delete()
    db.session.commit()
    return redirect("/users")


    