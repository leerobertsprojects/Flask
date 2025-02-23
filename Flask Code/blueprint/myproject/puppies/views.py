from flask import Blueprint, render_template, url_for, redirect
from myproject import db
from myproject.puppies.forms import AddForm, DelForm
from myproject.models import Puppy

puppy_blueprint = Blueprint('puppies', __name__, template_folder='templates/puppies')


@puppy_blueprint.route('/add', methods=['GET', 'POST'])
def add():

    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()
        return redirect(url_for('puppies.list'))

    return render_template('add.html', form=form)

@puppy_blueprint.route('/list')
def list():

    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)

@puppy_blueprint.route('/delete', methods=['GET', 'POST'])
def delete():

    form = DelForm()
    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('puppies.list'))

    return render_template('delete.html', form=form)
