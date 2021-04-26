"""Models for Blogly."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import delete
from datetime import datetime

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class User(db.Model):
    """Class for a user in the Blogly app."""

    __tablename__ = "user"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String(15),
                     nullable=False)
    last_name = db.Column(db.String(15), nullable=False)
    image_url = db.Column(db.String, 
                          nullable=True, 
                          default='https://unsplash.com/photos/fIq0tET6llw')

    def __repr__(self):
        """Show info about user."""

        u = self
        return f"<User {u.id} {u.first_name} {u.last_name} {u.image_url}>"
    
    def get_full_name(self):
        """Displays user's full name."""

        u = self
        return f"{u.first_name} {u.last_name}"
    
    def delete_user_info(self):
        """Deletes the info for a user."""

        u = self
        return user.delete(u)


class Post(db.Model):
    """Class for a user's post in the Blogly app."""

    __tablename__ = "post"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    title = db.Column(db.String,
                        nullable=False,
                        unique=True)
    content = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    user_id = db.Column(db.Integer, 
                        db.ForeignKey('user.id'))

    user = db.relationship('User', backref='posts')
    
    def __repr__(self):
        """Show info about user."""

        p = self
        return f"<Post {p.id} {p.title} {p.content} {p.created_at} {p.user_id}>"
    
    def format_date(self):
        """Format date nicely for post."""

        p = self
        date = p.created_at.strftime("%c")
        return f"{date}"    

class PostTag(db.Model):
    """Class for tags on a specific post in the Blogly app."""

    __tablename__ = "posttag"

    post_id = db.Column(db.Integer,
                        db.ForeignKey('post.id'),
                        primary_key=True,
                        nullable=False)
    tag_id = db.Column(db.Integer, 
                        db.ForeignKey('tag.id'),
                        primary_key=True,
                        nullable=False)

    post = db.relationship('Post', backref='posttags')
    tags = db.relationship('Tag', backref='posttags')

    def __repr__(self):
        """Show info about post tag."""

        p = self
        return f"<PostTag {p.post_id} {p.tag_id}>"



class Tag(db.Model):
    """Class for tags in the Blogly app."""

    __tablename__ = "tag"

    id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)
    name = db.Column(db.String, 
                        nullable=False)

    def __repr__(self):
        """Show info about tag."""

        t = self
        return f"<Tag {t.id} {t.name}>"
