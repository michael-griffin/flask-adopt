"""Flask app for adopt app."""

import os

from flask import Flask, render_template, flash, redirect, jsonify
from flask_debugtoolbar import DebugToolbarExtension
import requests
from models import connect_db, Pet, db, DEFAULT_IMAGE_URL
from forms import AddPetForm, EditPetForm
from petfinder import update_auth_token, PETFINDER_URL


app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")


connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)



auth_token = None

def refresh_credentials():
    """Just once, get token and store it globally."""
    global auth_token
    auth_token = update_auth_token()
    print(f'auth token is now: \n{auth_token}')


# with app.app_context seems to trigger on file changes.
# not sure what happens when you have this as a production
with app.app_context():
    refresh_credentials()


@app.get("/random")
def show_pet_info():
    """Return page about book."""

    resp = requests.get(PETFINDER_URL,
        headers = {"Authorization" : f"Bearer {auth_token}"},
        params={"limit": 20})

    pet_data = resp.json()
    print(f"random pets are: {pet_data}")
    # using the APIs JSON data, render full HTML page
    #return render_template("book_info.html", book=book_data)
    return jsonify(pet_data)


#Once we get auth token:
#The request header has the form Authorization: Bearer <Oauth Token>

@app.get('/')
def display_homepage():
    """ displays homepage"""
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/add', methods = ['GET', 'POST'])
def handle_add_pet_form():
    """displays add pet form; on submit validates and processes form"""
    form = AddPetForm()

    if form.validate_on_submit():

        pet = Pet(
            name=form.name.data,
            species=form.species.data,
            photo_url=form.photo_url.data or None,
            age=form.age.data,
            notes=form.notes.data)

        db.session.add(pet)
        db.session.commit()

        flash("pet added!")
        return redirect('/')

    else:
        return render_template('add-pet-form.html', form = form)



@app.route('/<int:pet_id>', methods = ['GET', 'POST'])
def handle_edit_pet_form(pet_id):
    """displays pet details and edit form. On submit, updates pet details."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        print("notes", form.notes.data, "available", form.available.data)
        pet.photo_url = form.photo_url.data or DEFAULT_IMAGE_URL
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        flash("Edit Success!")

        return redirect(f'/{pet.id}')
    else:
        return render_template('pet_detail.html', pet=pet, form=form)
