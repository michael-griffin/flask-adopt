"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, AnyOf

class AddPetForm(FlaskForm):
    '''Form for adding a pet'''
    name = StringField("Pet Name",
                       validators=[InputRequired()])
    species = StringField("Species",
                validators=[InputRequired(), AnyOf(["cat", "dog","porcupine"])])
    photo_url = StringField("Image",
                    validators=[Optional(), URL()]
                )
    age = SelectField("Age",
                choices = [('baby','Baby'), ('young','Young'),
                            ('adult','Adult'), ('senior', 'Senior')],
                validators=[InputRequired(),
                            AnyOf(["baby", "young","adult", "senior"])]
            )
    notes = StringField("Notes")
    #FIXME: TextAreaField


class EditPetForm(FlaskForm):
    '''Form for editing a pet'''
    photo_url = StringField("Image",
                    validators=[Optional(), URL()]
                )
    notes = StringField("Notes")
    available = BooleanField("Available")
