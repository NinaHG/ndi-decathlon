# IMPORTS #####################################################################
import sys

import jinja2
from flask import render_template, request, redirect

from app import app
import requests


# ROUTES ######################################################################
@app.route("/decathlon")
def wiki_home():
    return render_template(
        template_name_or_list="page/decathlon/wiki_home.html"
    )


@app.route("/decathlon/groups")
def all_groups():
    groups = []
    r = requests.get('https://sports.api.decathlon.com/groups/', headers={'Accept-Language': 'fr-FR'})
    if r.status_code == 200:
        groups = r.json()['data']
    return render_template(
        template_name_or_list="page/decathlon/group_list.html",
        groups=groups
    )


@app.route("/decathlon/groups/<int:group_id>")
def group_desc(group_id):
    group = {}
    sports = []
    r = requests.get('https://sports.api.decathlon.com/groups/' + str(group_id), headers={'Accept-Language': 'fr-FR'})
    if r.status_code == 200:
        group = r.json()['data']
        sports_data = group['relationships']['sports']['data']
        for sport in sports_data:
            r = requests.get('https://sports.api.decathlon.com/sports/' + str(sport['id']),
                             headers={'Accept-Language': 'fr-FR'})
            if r.status_code == 200:
                content = r.json()['data']
                sports.append({
                    'id': content['id'],
                    'name': content['attributes']['name']
                })
    return render_template(
        template_name_or_list="page/decathlon/group.html",
        group=group,
        sports=sports
    )


@app.route("/decathlon/sports")
def all_sports():
    sports = []
    r = requests.get('https://sports.api.decathlon.com/sports/', headers={'Accept-Language': 'fr-FR'})
    if r.status_code == 200:
        sports = r.json()['data']
    return render_template(
        template_name_or_list="page/decathlon/sport_list.html",
        sports=sports
    )


def get_sport(sport_id):
    sport = {}
    r = requests.get('https://sports.api.decathlon.com/sports/' + str(sport_id), headers={'Accept-Language': 'fr-FR'})
    if r.status_code == 200:
        sport = r.json()['data']
    return sport


@app.route("/decathlon/sports/<int:sport_id>")
def sport_desc(sport_id):
    sport = get_sport(sport_id)
    image_url = ''
    image_data = sport['relationships']['images']['data']
    if (len(image_data) > 0):
        image_url = image_data[0]['url']

    children = []
    related_list = []

    for related in sport['relationships']['children']:
        try:
            children.append(get_sport(related['data']['id']))
        except TypeError:
            pass
    for related in sport['relationships']['related']:
        try:
            exist = False
            related_id = related['data']['id']
            for child in children:
                if child['id'] == related_id:
                    exist = True
                    break
            if not exist:
                related_list.append(get_sport(related['data']['id']))
        except TypeError:
            pass

    return render_template(
        template_name_or_list="page/decathlon/sport.html",
        sport=sport,
        image_url=image_url,
        children=children,
        related_list=related_list
    )


@app.route("/decathlon/search")
def search_wiki():
    query = request.args.get('search')
    if not query:
        query = ''
    results = []
    r = requests.get('https://sports.api.decathlon.com/sports?q=' + query, headers={'Accept-Language': 'fr-FR'})
    if r.status_code == 200:
        results = r.json()['data']
    return render_template(
        template_name_or_list="page/decathlon/search_result.html",
        query=query,
        sports=results
    )


@app.route("/decathlon/search?search=<string:query>")
def search_tag_wiki(query):
    results = []
    r = requests.get('https://sports.api.decathlon.com/sports?q=' + query, headers={'Accept-Language': 'fr-FR'})
    if r.status_code == 200:
        results = r.json()['data']
    return render_template(
        template_name_or_list="page/decathlon/search_result.html",
        query=query,
        sports=results
    )