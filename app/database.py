# IMPORTS #####################################################################
from flask_sqlalchemy import SQLAlchemy

from .app import app
from .config import SQLiteConfig


# DATABASE ####################################################################
# Configure database information in application.
app.config.from_object(SQLiteConfig)
# Create database with it configuration saved in application.
db = SQLAlchemy(app)