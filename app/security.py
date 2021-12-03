# IMPORTS #####################################################################
from flask_security import Security, SQLAlchemyUserDatastore
from flask_security.cli import roles_create, roles_add, users_create
from click.testing import CliRunner

from .app import app
from .database import db
from .model import security, bateau, sauvetage
from .form.security import AuthRegisterForm, AuthLoginForm
from .config import SecurityDevConfig
from .cli.database import is_database_exist, create_database


# SECURITY ####################################################################
app.config.from_object(SecurityDevConfig)
user_datastore = SQLAlchemyUserDatastore(db, security.User, security.Role)
security = Security(
	app=app,
	datastore=user_datastore,
	register_form=AuthRegisterForm,
	login_form=AuthLoginForm,
)


# DATABASE INITIALISATION #####################################################
cli = CliRunner()

# création de la base de données si elle n'existe pas encore
if not is_database_exist():
	# créer la base de données
	cli.invoke(cli=create_database)
	# créer l'administrateur initial
	cli.invoke(cli=users_create, args=[
		f"email:{SecurityDevConfig.SECURITY_DEFAULT_ADMIN_EMAIL}",
		f"first_name:{SecurityDevConfig.SECURITY_DEFAULT_ADMIN_FIRST_NAME}",
		f"last_name:{SecurityDevConfig.SECURITY_DEFAULT_ADMIN_LAST_NAME}",
		"--password", SecurityDevConfig.SECURITY_DEFAULT_ADMIN_PASSWORD,
		"-a"
	])
	# créer le rôle de l'administrateur
	cli.invoke(cli=roles_create, args=[SecurityDevConfig.SECURITY_ADMIN_ROLE])
	# associer le rôle d'administration à l'administrateur initial
	cli.invoke(cli=roles_add, args=[SecurityDevConfig.SECURITY_DEFAULT_ADMIN_EMAIL, SecurityDevConfig.SECURITY_ADMIN_ROLE])


# CONTEXT PROCESSORS ##########################################################
@app.context_processor
def inject_admin_role():
	return dict(admin_role=SecurityDevConfig.SECURITY_ADMIN_ROLE)