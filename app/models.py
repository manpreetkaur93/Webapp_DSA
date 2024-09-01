'''Denna fil innehåller databasmodeller, som är Python-klasser som representerar tabeller i din databas.
Om du använder en ORM (Object-Relational Mapping) som SQLAlchemy, definieras varje tabell i databasen som en klass i den här filen.'''
from flask_sqlalchemy import SQLAlchemy
from faker import Faker

db = SQLAlchemy()
fake = Faker()

class Person(db.Model):
    __tablename__ = 'persons'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    personnummer = db.Column(db.String(12), unique=True, nullable=False)
    city = db.Column(db.String(255), nullable=False)
    country = db.Column(db.String(255), nullable=False)
    profession = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(30), nullable=False)
    is_celebrity = db.Column(db.Boolean, default=False)

def generate_unique_personnummer():
    """Genererar ett unikt personnummer."""
    while True:
        personnummer = fake.ssn()
        if not Person.query.filter_by(personnummer=personnummer).first():
            return personnummer

def generate_person(is_celebrity=False):
    """Genererar en ny person med falska data och anger om personen är en kändis."""
    if is_celebrity:
        # Generera en kändis med ett känt namn
        name = fake.first_name_female() if fake.boolean() else fake.first_name_male()
        name += ' ' + fake.last_name()
    else:
        name = fake.name()

    return Person(
        name=name,
        personnummer=generate_unique_personnummer(),
        city=fake.city(),
        country=fake.country(),
        profession="Actor" if is_celebrity else fake.job(),
        phone_number=fake.phone_number()[:15],
        is_celebrity=is_celebrity
    )

def seed_database(n=100000):
    """Skapar och sparar n antal personer i databasen, inklusive en andel kändisar."""
    people = []
    # Generera 10% kändisar
    for _ in range(int(n * 0.1)):
        person = generate_person(is_celebrity=True)
        people.append(person)
    # Generera resterande vanliga personer
    for _ in range(n - len(people)):
        person = generate_person()
        people.append(person)
    
    db.session.bulk_save_objects(people)
    db.session.commit()
    print(f"Seedade {n} personer till databasen.")

def clear_table():
    """Tömmer Person-tabellen."""
    db.session.query(Person).delete()
    db.session.commit()
