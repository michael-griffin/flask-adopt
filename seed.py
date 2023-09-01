from app import app, db
from models import DEFAULT_IMAGE_URL, Pet

db.drop_all()
db.create_all()

# For testing database initially
sundance = Pet(name='Sundance', species="dog",
               photo_url="https://upload.wikimedia.org/wikipedia/"\
                "commons/d/d5/Retriever_in_water.jpg",
               age="adult"
               )
jocelyn = Pet(name='Jocelyn', species="porcupine",
               photo_url=
               "https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/"\
                "Porcupine_%285670622729%29.jpg/"\
                    "440px-Porcupine_%285670622729%29.jpg",
               age="adult",
               notes="medium big"
               )

db.session.add(sundance)
db.session.add(jocelyn)
db.session.commit()
