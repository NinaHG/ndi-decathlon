# IMPORTS #####################################################################
from flask_security import RegisterForm
from wtforms import (StringField,HiddenField)
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from wtforms.fields  import (BooleanField,DateField)


# FORMS #######################################################################

class PersonneForm(FlaskForm):
    id      = HiddenField('pers_id')
    nom    = StringField("nom", validators=[DataRequired()])
    prenom = StringField("prenom", validators=[DataRequired()])
    #pers_creation = DateField("creation compte",format='%m/%d/%Y')
    date_naissance = DateField("date de naissance")
    date_deces = DateField("date de deces")
    sauvetage = BooleanField("sauvetage")
    #valide_pers = BooleanField("valide_pers")
