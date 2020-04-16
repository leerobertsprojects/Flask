from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):

    id = IntegerField('ID number of puppy ')
    name = StringField('Enter Owners Name: ')
    submit = SubmitField('submit')
