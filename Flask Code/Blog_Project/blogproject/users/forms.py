from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo
from flask_wtf.file import FileField, FileAllowed

from flask_login import current_user
from blogproject.models import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_pass = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already')

    def check_usxername(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Your Username has been registered already please choose a different one')

class UpdateUserForm(FlaskForm):
    email = StringField('Update Email', validators=[Email()])
    username = StringField('Update Username')
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already')

    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Your Username has been registered already please choose a different one')
