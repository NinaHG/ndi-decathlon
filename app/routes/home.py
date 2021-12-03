# IMPORTS #####################################################################
from flask import render_template

from app import app
from app.model.bateau import getAllBateaux, getBateauById
from app.model.sauvetage import (getPersonne, all_personne)


# ROUTES ######################################################################
@app.route("/")
def home():
	return render_template(
		template_name_or_list="page/home.html"
	)

@app.route("/pimp")
def pimp():
	return render_template(
		template_name_or_list="page/pimp.html"
	)


@app.route("/personne")
def personne():
	return render_template(
		personnes=all_personne(),
		template_name_or_list="page/home/personne.html"
	)


@app.route("/personne/<int:id>")
def personne_detail(id):
    return render_template(
        personne=getPersonne(id),
        template_name_or_list="page/home/personne_detail.html"
    )


@app.route("/bateau")
def bateau():
    return render_template(
        template_name_or_list="page/home/bateau.html",
        bateaux=getAllBateaux()
    )


@app.route("/bateau/<int:id>")
def bateau_detail(id):
    return render_template(
        template_name_or_list="page/home/bateau_detail.html",
        bateau=getBateauById(id)
    )


@app.route("/sauvetage")
def sauvetage():
    return render_template(
        template_name_or_list="page/home/sauvetage.html"
    )


@app.route("/sauvetage/<int:id>")
def sauvetage_detail(id):
    return render_template(
        template_name_or_list="page/home/sauvetage_detail.html"
    )
