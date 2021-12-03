# IMPORTS #####################################################################
from wtforms import StringField, BooleanField, SubmitField, HiddenField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


# FORMS #######################################################################
class PersonneAdminForm(FlaskForm):
    submit = SubmitField("Valider")