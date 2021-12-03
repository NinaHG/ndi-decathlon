# IMPORTS #####################################################################
from flask_security import RegisterForm, LoginForm
from wtforms import StringField
from wtforms.validators import DataRequired


# FORMS #######################################################################
class AuthRegisterForm(RegisterForm):
	first_name = StringField(label="First Name", validators=[DataRequired()])
	last_name = StringField(label="Last Name", validators=[DataRequired()])


class AuthLoginForm(LoginForm):
	pass