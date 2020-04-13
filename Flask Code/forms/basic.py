from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):
    # breed = StringField("<h2>What breed are you: </h2>")
    first = StringField('First Name')
    last = StringField('Last Name')
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    # breed = False
    form = InfoForm()
    first = False
    last = False
    if form.validate_on_submit():
        first = form.first.data
        last = form.last.data
        form.first.data = ''
        form.last.data = ''

    # if form.validate_on_submit():
    #     breed = form.breed.data
    #     form.breed.data = ''
    return render_template('index.html', form=form, first=first, last=last)


if __name__ == '__main__':
    app.run(debug=True)
