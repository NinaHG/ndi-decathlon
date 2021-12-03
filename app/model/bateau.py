from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, func

from app import db


class Bateau(db.Model):
    __tablename__ = "bateau"
    bat_id = Column(Integer(), primary_key=True)
    bat_creation = Column(DateTime(), primary_key=True, nullable=False)
    nom = Column(String(255), nullable=False)
    sauvetage = Column(Boolean(), nullable=False)
    valide_bat = Column(Boolean(), nullable=False)


def getMaxIdBateau():
    id = db.session.query(func.max(Bateau.bat_id)).scalar()
    return id if id else 0


def getAllBateaux():
    return Bateau.query.all()


def getBateauById(id):
    return Bateau.query.filter(Bateau.bat_id == id).all()[0]

def AllBateauPasValider():
    return  Bateau.query.filter(Bateau.valide_bat==False).all()