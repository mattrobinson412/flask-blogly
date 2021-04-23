"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import delete

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
                     nullable=False,
                     unique=True)
    last_name = db.Column(db.String(15), nullable=False)
    image_url = db.Column(db.String, 
                          nullable=True, 
                          default='https://unsplash.com/photos/fIq0tET6llw')

    # @validates('first_name')
    # def validate_first_name(self, key, val):
    #     assert int not in val
    #     return val
    
    # @validates('last_name')
    # def validate_last_name(self, key, val):
    #     assert int not in val
    #     return val
    
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


    
