from app import app, db
from models import DEFAULT_IMAGE_URL, Pet

db.drop_all()
db.create_all()

# For testing database initially
sundance = Pet(name='Sundance', species="dog",
               photo_url="/static/puppy.png",
               age="adult"
               )
jocelyn = Pet(name='Jocelyn', species="porcupine",
               photo_url="/static/porcupine.png",
               age="adult",
               notes="medium big"
               )

db.session.add(sundance)
db.session.add(jocelyn)
db.session.commit()




