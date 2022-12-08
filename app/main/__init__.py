from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
from ..models import Permission

@main.app_context_processor
def inject_permissions():
    """ Make the permissions available to all of the templates using the app 'context processor' """
    return dict(Permission=Permission)
