# IMPORTS #####################################################################
from .app import app                            # app
from .database import db                        # database
from .env import env                            # environment
from .security import user_datastore, security  # authentication auth

from . import wsgi      # proxy                                 | module
from . import cli       # custom Flask command line interface   | package
from . import model     # tables saved in database              | package
from . import routes    # routes for each views (URL)           | package

