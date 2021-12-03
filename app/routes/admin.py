# IMPORTS #####################################################################
from flask import render_template
from flask_security import auth_required
from app.form.admin import PersonneAdminForm
from app import app, db
from app.model.sauvetage import AllPersonnePasValider,getPersonne
from app.model.bateau import AllBateauPasValider,getBateauById
from flask import render_template, request, redirect, url_for

# ROUTES ######################################################################
METHOD_GET = "GET"
METHOD_POST = "POST"

@app.route("/admin")
@auth_required()
def admin():
	return render_template(
		personnes = AllPersonnePasValider(),
		bateaux = AllBateauPasValider(),
		template_name_or_list="page/admin/admin.html"
	)

@app.route("/admin/personne/<int:id>",methods=[METHOD_GET, METHOD_POST])
@auth_required()
def admin_personne(id):
	p = getPersonne(id)
	f = PersonneAdminForm()
	print(f.data)
	if f.validate_on_submit():
		print("ok")
		p.valide_pers =True
		db.session.add(p)
		db.session.commit()
		return redirect(url_for('admin'))
	return render_template(
		form =f,
		personne = getPersonne(id),
		template_name_or_list="page/admin/admin_personne.html"
	)

@app.route("/admin/bateau/<int:id>",methods=[METHOD_GET, METHOD_POST])
@auth_required()
def admin_bateau(id):
	p = getBateauById(id)
	f = PersonneAdminForm()
	print(f.data)
	if f.validate_on_submit():
		print("ok")
		p.valide_bat =True
		db.session.add(p)
		db.session.commit()
		return redirect(url_for('admin'))
	return render_template(
		form = f,
		bateau =p,
		template_name_or_list="page/admin/admin_bateau.html"
	)

@app.route("/admin/sauvetage/<int:id>")
@auth_required()
def admin_sauvetage(id):
	return render_template(
		template_name_or_list="page/admin/admin_sauvetage.html"
	)