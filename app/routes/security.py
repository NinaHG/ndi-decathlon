# IMPORTS #####################################################################
from flask import render_template, redirect, url_for, request
from flask_security import hash_password

from app import app, db, security, user_datastore
from . import home


# CONSTANTS ###################################################################
METHOD_GET = "GET"
METHOD_POST = "POST"


# ROUTES ######################################################################
@app.route("/register", methods=[METHOD_GET, METHOD_POST])
def register():
	register_form = security.register_form()
	# if method POST
	if request.method == METHOD_POST and register_form.is_submitted() and register_form.validate_on_submit():
		user_datastore.create_user(
			email=register_form.email.data,
			password=hash_password(register_form.password.data),
			first_name=register_form.first_name.data.lower(),
			last_name=register_form.last_name.data.lower()
		)
		db.session.commit()
		return redirect(url_for(home.home.__name__))
	# if method GET
	return render_template(
		template_name_or_list="page/security/register.html",
		register_form=register_form
	)