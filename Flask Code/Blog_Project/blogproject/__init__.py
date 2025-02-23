import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager



################ initialize app ########################
app = Flask(__name__)

############### database setup ###########################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)
###############login Configuration#####################

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'

###############blueprints setup##########################
from blogproject.core.views import core
from blogproject.error_pages.handlers import error
from blogproject.users.views import users
from blogproject.blogposts.views import blog_posts

app.register_blueprint(core)
app.register_blueprint(error)
app.register_blueprint(users)
app.register_blueprint(blog_posts)








