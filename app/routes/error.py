# IMPORTS #####################################################################
from flask import render_template

from app import app


# ROUTES ######################################################################
@app.errorhandler
def error_others(error):
	"""The Others"""
	return render_template(
		template_name_or_list="page/error/error_others.html",
		error=error
	), error.code


@app.errorhandler(401)
def error_401(error):
	"""Unauthorized"""
	return render_template(
		template_name_or_list="page/error/error_401.html",
		error=error
	), error.code


@app.errorhandler(403)
def error_403(error):
	"""Forbidden"""
	return render_template(
		template_name_or_list="page/error/error_403.html",
		error=error
	), error.code


@app.errorhandler(404)
def error_404(error):
	"""Not Found"""
	return render_template(
		template_name_or_list="page/error/error_404.html",
		error=error
	), error.code


@app.errorhandler(500)
def error_500(error):
	"""Internal Server Error"""
	return render_template(
		template_name_or_list="page/error/error_500.html",
		error=error
	), error.code