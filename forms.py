"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField

class AddPetForm(FlaskForm):
	#name, price corresponds to name of the to be created input
	#string in field's parentheses correspond to the LABEL of the input
    name = StringField("Pet Name")
    species = StringField("Species")
    photo_url = StringField("Image")
    age = SelectField("Age",
                choices = ['baby', 'young', 'adult', 'senior'])
    notes = StringField("Notes")
