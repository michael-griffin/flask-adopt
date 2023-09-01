"""Flask app for adopt app."""

import os

from flask import Flask, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, Pet, db
from forms import AddPetForm, EditPetForm

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


@app.get('/')
def display_homepage():
    '''displays homepage'''

    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/add', methods = ['GET', 'POST'])
def handle_add_pet_form():
    '''displays add pet form, on submit validates and processes form'''

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

        return redirect('/')

    else:
        return render_template('add-pet-form.html', form = form)





@app.route('/<int:pet_id>', methods = ['GET', 'POST'])
def handle_edit_pet_form(pet_id):
    '''displays add pet form, on submit validates and processes form'''

    pet = Pet.query.get(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():

        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()

        return redirect(f'/{pet_id}')
    else:
        return render_template('pet_detail.html', pet=pet, form=form)