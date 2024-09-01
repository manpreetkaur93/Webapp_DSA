'''Denna fil innehåller databasmodeller, som är Python-klasser som representerar tabeller i din databas.
Om du använder en ORM (Object-Relational Mapping) som SQLAlchemy, definieras varje tabell i databasen som en klass i den här filen.'''
from flask_sqlalchemy import SQLAlchemy
from faker import Faker

db = SQLAlchemy()
fake = Faker()

class Person(db.Model):
    __tablename__ = 'persons'  # Specificera att modellen ska använda tabellen 'persons'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    personnummer = db.Column(db.String(12), unique=True, nullable=False)
    city = db.Column(db.String(255), nullable=False)
    country = db.Column(db.String(255), nullable=False)
    profession = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(30), nullable=False)


def generate_person():
    """Genererar en ny person med falska data."""
    return Person(
        name=fake.name(),
        personnummer=fake.ssn(),
        city=fake.city(),
        country=fake.country(),
        profession=fake.job(),
        phone_number=fake.phone_number()
    )

def seed_database(n=1000):
    """Skapar och sparar n antal personer i databasen."""
    people = []
    for _ in range(n):
        person = generate_person()
        people.append(person)
    db.session.bulk_save_objects(people)
    db.session.commit()
    print(f"Seedade {n} personer till databasen.")
