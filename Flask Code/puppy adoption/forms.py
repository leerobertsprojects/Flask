from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):

    name = StringField('Please enter puppy name')
    submit = SubmitField('Submit')


class DelForm(FlaskForm):

    id = IntegerField('ID number of puppy')
    submit = SubmitField('Submit')

class AddOwnerForm(FlaskForm):

    id = IntegerField('ID number of puppy ')
    name = StringField('Enter Owners Name: ')
    submit = SubmitField('submit')



