# IMPORTS #####################################################################
from werkzeug.middleware.proxy_fix import ProxyFix

from .app import app


# PROXY #######################################################################
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1)