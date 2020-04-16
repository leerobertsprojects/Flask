from flask import render_template, redirect, url_for, Blueprint
from myproject import db
from myproject.models import Owner
from myproject.owners.forms import AddForm

owners_blueprints = Blueprint('owners', __name__, template_folder='templates/owners')

@owners_blueprints.route('/add',methods=['GET','POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        id = form.id.data
        owner = Owner(name, id)
        db.session.add(owner)
        db.session.commit()

        return redirect(url_for('puppies.list'))
    return render_template('owner.html', form=form)