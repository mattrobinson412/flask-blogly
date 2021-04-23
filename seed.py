"""Seed file to make sample data for user db."""

from models import User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add pets
feeny = User(first_name='Feeny', 
                last_name="Josefin", 
                image_url='https://unsplash.com/photos/ILip77SbmOE')
lenny = User(first_name='Lenny', 
                last_name="Raleway", 
                image_url='https://unsplash.com/photos/_7LbC5J-jw4')
kai = User(first_name='Kai', 
                last_name="Montserrat", 
                image_url='https://unsplash.com/photos/At__EKm5PGE')

# Add new objects to session, so they'll persist
db.session.add(feeny)
db.session.add(lenny)
db.session.add(kai)

# Commit--otherwise, this never gets saved!
db.session.commit()
