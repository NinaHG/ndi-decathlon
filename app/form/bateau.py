# IMPORTS #####################################################################
from wtforms import StringField, BooleanField, SubmitField, HiddenField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


# FORMS #######################################################################
class BateauForm(FlaskForm):
    bat_id = HiddenField()
    nom = StringField(label="Nom du bateau", validators=[DataRequired()])
    sauvetage = BooleanField(label="Bateau de sauvetage ?")
    valide_bat = BooleanField(label="valider")
    submit = SubmitField("Créer")