import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from myproject.puppies.views import puppy_blueprint
from myproject.owners.views import owners_blueprints
app.register_blueprint(owners_blueprints, url_prefix="/owners")
app.register_blueprint(puppy_blueprint, url_prefix="/puppies")

Migrate(app, db)

