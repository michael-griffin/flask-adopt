"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import InputRequired, Optional, URL

class AddPetForm(FlaskForm):
    name = StringField("Pet Name")
    species = StringField("Species")
    photo_url = StringField("Image")
    age = SelectField("Age",
                choices = [('baby','Baby'), ('young','Young'),
                            ('adult','Adult'), ('senior', 'Senior')])
    notes = StringField("Notes")
