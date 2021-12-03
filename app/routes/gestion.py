# IMPORTS #####################################################################
from flask import render_template, request, redirect, url_for, abort
from flask_security import auth_required
from app.form.bateau import BateauForm
from app.form.personne import PersonneForm
from app.model.bateau import Bateau, getMaxIdBateau, getBateauById
from app.model.sauvetage import Personne
from app.routes import home
from datetime import datetime
from app import app, db
from app.model.sauvetage import (max_id_personne, getPersonne)

METHOD_GET = "GET"
METHOD_POST = "POST"


# ROUTES ######################################################################
@app.route("/gestion/personne", methods=[METHOD_GET, METHOD_POST])
@auth_required()
def gestion_personne_create():
    f = PersonneForm()
    if f.validate_on_submit():
        id = max_id_personne()
        a = Personne(pers_id=id, nom=f.nom.data, prenom=f.prenom.data, pers_creation=datetime.now(),
                     date_deces=f.date_deces.data, date_naissance=f.date_naissance.data, sauvetage=f.sauvetage.data,
                     valide_pers=False)
        db.session.add(a)
        db.session.commit()
        return redirect(url_for('personne_detail', id=int(id)))
    return render_template(
        form=f,
        template_name_or_list="page/gestion/gestion_personne_create.html"
    )


@app.route("/gestion/personne/<int:id>", methods=[METHOD_GET, METHOD_POST])
@auth_required()
def gestion_personne_edit(id):
    try:
        p = getPersonne(id)
        f = PersonneForm(id=p.pers_id, nom=p.nom, prenom=p.prenom, date_deces=p.date_deces, date_naissance=p.date_naissance,
                         sauvetage=p.sauvetage)
        if f.validate_on_submit():
            id = p.pers_id
            p = Personne(pers_id=id, nom=f.nom.data, prenom=f.prenom.data, pers_creation=datetime.now(),
                         date_deces=f.date_deces.data, date_naissance=f.date_naissance.data, sauvetage=f.sauvetage.data,
                         valide_pers=False)
            db.session.add(p)
            db.session.commit()
            return redirect(url_for('personne_detail', id=int(id)))
    except:
        abort(404)
    return render_template(
        personne=p,
        form=f,
        template_name_or_list="page/gestion/gestion_personne_edit.html"
    )


@app.route("/gestion/bateau", methods=[METHOD_GET, METHOD_POST])
@auth_required()
def gestion_bateau_create():
    bateau_form = BateauForm()
    # if method POST
    if request.method == METHOD_POST and bateau_form.is_submitted() and bateau_form.validate_on_submit():
        bateau = Bateau(bat_id=getMaxIdBateau() + 1,
                        bat_creation=datetime.now(),
                        nom=bateau_form.nom.data,
                        sauvetage=bateau_form.sauvetage.data,
                        valide_bat=0,
                        )
        db.session.add(bateau)
        db.session.commit()
        return redirect(url_for(home.bateau_detail.__name__, id=bateau.bat_id))
    # if method GET
    return render_template(
        template_name_or_list="page/gestion/gestion_bateau_create.html",
        bateau_form=bateau_form
    )


@app.route("/gestion/bateau/<int:id>", methods=["GET", "POST"])
@auth_required()
def gestion_bateau_edit(id):
    try:
        bateau = getBateauById(id)
        bateau_form = BateauForm(bat_id=bateau.bat_id,
                                 nom=bateau.nom,
                                 sauvetage=bateau.sauvetage,
                                 )
        # if method POST
        if request.method == METHOD_POST and bateau_form.is_submitted() and bateau_form.validate_on_submit():
            bateau = Bateau(bat_id=id,
                            bat_creation=datetime.now(),
                            nom=bateau_form.nom.data,
                            sauvetage=bateau_form.sauvetage.data,
                            valide_bat=0,
                            )
            db.session.add(bateau)
            db.session.commit()
            return redirect(url_for(home.bateau_detail.__name__, id=bateau.bat_id))
    except:
        abort(404)
    # if method GET
    return render_template(
        template_name_or_list="page/gestion/gestion_bateau_edit.html",
        bateau_form=bateau_form
    )


@app.route("/gestion/sauvetage")
@auth_required()
def gestion_sauvetage_create():
    return render_template(
        template_name_or_list="page/gestion/gestion_sauvetage_create.html"
    )


@app.route("/gestion/sauvetage/<int:id>")
@auth_required()
def gestion_sauvetage_edit(id):
    return render_template(
        template_name_or_list="page/gestion/gestion_sauvetage_edit.html"
    )
