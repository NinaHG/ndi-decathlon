from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy import func
from app import db


class Personne(db.Model):
    __tablename__ = "personne"
    pers_id = Column(Integer(), primary_key=True)
    pers_creation = Column(DateTime(), primary_key=True,nullable=False)
    nom = Column(String(255))
    prenom = Column(String(255))
    date_naissance = Column(DateTime())
    date_deces = Column(DateTime())
    sauvetage = Column(Boolean(), nullable=False)
    valide_pers = Column(Boolean(), nullable=False)


class Status(db.Model):
    __tablename__ = "status"
    status_id = Column(Integer(), primary_key=True)
    intitule = Column(String(255))


class Compose(db.Model):
    __tablename__ = "compose"
    compose_id = Column(Integer(), primary_key=True)
    valide_status = Column(Boolean(), primary_key=True, nullable=False)
    pers_id = Column('pers_id', Integer(), ForeignKey('personne.pers_id'))
    bat_id = Column('bat_id', Integer(), ForeignKey('bateau.bat_id'))
    status_id = Column('status_id', Integer(), ForeignKey('status.status_id'))


class Sauvetage(db.Model):
    __tablename__ = "sauvetage"
    sauve_id = Column(Integer(), primary_key=True)
    sauve_creation = Column(DateTime(), primary_key=True, nullable=False)
    coord_gps = Column(String(255))
    date_sauve = Column(DateTime(), nullable=False)
    desc = Column(String(255))
    valide_sauve = Column(Boolean(), nullable=False)

    bat1_id = Column('bat_sauveteur_id', Integer(), ForeignKey('bateau.bat_id'))
    bat2_id = Column('bat_secourus_id', Integer(), ForeignKey('bateau.bat_id'))

def getPersonne(id):
    return  Personne.query.filter(Personne.pers_id == id).all()[0]


def max_id_personne():
    max_logins = db.session.query(func.max(Personne.pers_id)).scalar()
    return max_logins if max_logins else 0

def all_personne():
    return Personne.query.all()

def AllPersonnePasValider():
    return  Personne.query.filter(Personne.valide_pers==False).all()

