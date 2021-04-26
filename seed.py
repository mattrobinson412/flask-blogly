"""Seed file to make sample data for user db."""

from models import User, db, Post, Tag, PostTag
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If tables aren't empty, empty them
User.query.delete()
Post.query.delete()
Tag.query.delete()
PostTag.query.delete()


# Add users
feeny = User(first_name='Feeny', 
                last_name="Josefin", 
                image_url='https://unsplash.com/photos/ILip77SbmOE')
lenny = User(first_name='Lenny', 
                last_name="Raleway", 
                image_url='https://unsplash.com/photos/_7LbC5J-jw4')
kai = User(first_name='Kai', 
                last_name="Montserrat", 
                image_url='https://unsplash.com/photos/At__EKm5PGE')

# Add and commit new objects to session, so they'll persist
db.session.add_all([feeny, lenny, kai])
db.session.commit()

# add posts
first_post = Post(title='Cooking Crab Legs Like a Cajun',
                    content='lorem ipsum fsdfad fsdafsdj fdsfkdsfj. fdsfj fsfdsf sdfdsf dfds.',
                    user_id=1)
second_post = Post(title='Marvelous Movies from the 90s.',
                    content='lorem ipsum fsdfad fsdafsdj fdsfkdsfj. fdsfj fsfdsf sdfdsf dfds.',
                    user_id=2)
third_post = Post(title='Remembering Finding Nemo from an Adult Perspective.',
                    content='lorem ipsum fsdfad fsdafsdj fdsfkdsfj. fdsfj fsfdsf sdfdsf dfds.',
                    user_id=3)

# Add and commit new objects to session, so they'll persist
db.session.add_all([first_post, second_post, third_post])
db.session.commit()

# add tags
tag = Tag(name='Literature')
tags = Tag(name='Poetry')
tagged = Tag(name='Satire')

# Add and commit new objects to session, so they'll persist
db.session.add_all([tag, tags, tagged])
db.session.commit()

# add post tags
tag = PostTag(post_id='1', tag_id='1')
tags = PostTag(post_id='2', tag_id='2')
tagged = PostTag(post_id='3', tag_id='3')

# Add and commit new objects to session, so they'll persist
db.session.add_all([tag, tags, tagged])
db.session.commit()