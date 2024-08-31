'''Denna fil innehåller databasmodeller, som är Python-klasser som representerar tabeller i din databas.
Om du använder en ORM (Object-Relational Mapping) som SQLAlchemy, definieras varje tabell i databasen som en klass i den här filen.'''
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    personnummer = db.Column(db.String(12), unique=True, nullable=False)
    city = db.Column(db.String(255), nullable=False)
    country = db.Column(db.String(255), nullable=False)
    profession = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
