# WWW

**dates:** 2 décembre (16h40) au 3 décembre (8h00)  
**principe:** concours de programmation de la Nuit de l'Info  
**sujet:** [PDF](sujet.pdf)  
___


## Table des matières
[[_TOC_]]

<br/><br>

## Objectif
<div style="color:#ffbf00; font-weight: bold">TODO: à faire</div>


<br/><br>

## Installation
### Téléchargement du projet
```sh
$ git clone https://gitlab.com/univ-orleans/m2/nuit-de-info/www.git
```


<br/><br>

## Environnement virtuel
### Création du venv
Le répertoire `venv` permet d'avoir un environnement python spécifique au projet. Ainsi, il contient toutes les librairies strictement nécessaires à l'application. Il n'est pas versionné et nécessite donc de maintenir une liste des librairies installées (voir [Librairies python](#librairies-python)).
#### Linux
```sh
$ cd www/
$ python3 -m venv venv
```
#### Windows
```sh
C:> cd www/
C:> py -m venv venv
```

### Activation / Désactivation
Pour utiliser l'environnement virtuel ou se placer de dans, il faut l'activer. La commande inverse permet de désactiver l'environnement virtuel ou d'en sortir.
#### Linux
```sh
$ source venv/bin/activate
$ # work...
$ deactivate
```
#### Windows
```sh
C:> venv\Scripts\activate.bat
C:> # work...
C:> venv\Scripts\deactivate.bat
```


<br/><br>

## Librairies python
### Installer les librairies du projet
À la récupération du projet ou suite à l'ajout d'une librairie par un tiers, il faut mettre à jour l'environnement 
virtuel  en installent les dépendances nouvellement ajoutées.
```sh
$ pip install -r requirements.txt
```

### Sauvegarder la liste des librairies
Pour sauvegarder la liste des librairies installées dans l'environnement virtuel, il faut les lister et les 
inscrire dans le fichier [requirements.txt](requirements.txt) avec la commande suivante.
```sh
$ pip freeze > requirements.txt
```


<br/><br>

## Execution du projet
Pour lancer le serveur, il est possible d'utiliser soit la commande `flask run` du micro-framework Flask, soit d'exécuter
directement le script python `run.py`. Les deux commandes sont équivalentes. Après avoir exécuté l'une de ces deux 
commandes, l'application démarre en affichent les logs dans la console et en activant le mode de débogage.  
L'application est donc accésible depuis cette URL: [http://127.0.0.1:5000](http://127.0.0.1:5000)


<br/><br>

## Prérequis logiciel
| Logiciel | Version | Documentation | Description |
| :-- | --: | :-- | :-- |
| Python | 3.8 | [www.python.org](https://www.python.org/downloads/release/python-380/) | Langage de programmation utilisé pour exécuter le projet. |
| Flask | 2.0.2 | [flask.palletsprojects.com](https://flask.palletsprojects.com/en/2.0.x/) | Microframework de développement web python. |
| SQLAlchemy | 1.4.27 | [www.sqlalchemy.org](https://www.sqlalchemy.org/) | ORM python. |


<br/><br>

## Contributeurs
- Arnaud ORLAY (@arnorlay) : Master 2 IMIS Informatique
- Marion JURÉ (@Marionjure) : Master 2 IMIS Informatique
- Nicolas ZHOU (@Zhou_Nicolas) : Master 2 IMIS Informatique
- My Nina HONG (@ninahg) : Master 2 IMIS Informatique
- Marie CHRISTOPHE (@Ysisse) : Master 2 MIAGE
- François-Hugues LABARBE (@FHLabarbe) : Licence 3 Ingénierie Informatique
- Rémi ZABROCKI (@Rozkub) : Licence 3 Ingénierie Informatique
- Florian TRÉMÉLO (@tremeloflorian) : Licence 3 Ingénierie Informatique