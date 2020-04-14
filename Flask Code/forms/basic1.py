from flask import Flask, render_template, session, flash, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

class SimpleForm(FlaskForm):

    breed = StringField('Please enter your breed: ')
    submit = SubmitField('Click Me.')

@app.route('/',methods=['GET', 'POST'])
def index():

    form = SimpleForm()
    if form.validate_on_submit():

        session['breed'] = form.breed.data
        flash(f'The breed you have chosen is {session["breed"]}')

        return redirect(url_for('index'))
    return render_template('index1.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
