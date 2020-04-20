from blogproject import app
from flask import render_template, Blueprint

error = Blueprint('error', __name__)


@error.app_errorhandler(404)
def error_404(e):
    return render_template('error_pages/404.html'), 404

@error.app_errorhandler(403)
def error_403(e):
    return render_template('error_pages/403.html'), 403
