from sqlalchemy import true
from utils.db import db

class Burgas(db.Model):
    id = db.Column(db.Integer, primary_key = true)
    nombreHamburguesa = db.Column(db.String)
    precioHamburguesa = db.Column(db.Integer)
    urlHamburguesa = db.Column(db.String)

    def __init__(self,nombreHamburguesa,precioHamburguesa,urlHamburguesa):
        self.nombreHamburguesa
        self.precioHamburguesa
        self.urlHamburguesa        