'''Denna fil innehåller databasmodeller, som är Python-klasser som representerar tabeller i din databas.
Om du använder en ORM (Object-Relational Mapping) som SQLAlchemy, definieras varje tabell i databasen som en klass i den här filen.'''
import time
from flask_sqlalchemy import SQLAlchemy
from faker import Faker
from sqlalchemy.exc import IntegrityError

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

def generate_unique_personnummer(existing_personnummers):
    """Genererar ett unikt personnummer och kontrollerar det mot en lokal lista."""
    while True:
        personnummer = fake.ssn()
        if personnummer not in existing_personnummers:
            existing_personnummers.add(personnummer)  # Lägg till i mängden för att undvika dubbletter
            return personnummer

def generate_person(existing_personnummers, is_celebrity=False):
    """Genererar en ny person med falska data och anger om personen är en kändis."""
    if is_celebrity:
        # Generera en kändis med ett mer realistiskt namn
        name = fake.first_name_female() if fake.boolean() else fake.first_name_male()
        name += ' ' + fake.last_name()
    else:
        name = fake.name()

    return Person(
        name=name,
        personnummer=generate_unique_personnummer(existing_personnummers),
        city=fake.city(),
        country=fake.country(),
        profession="Actor" if is_celebrity else fake.job(),
        phone_number=fake.phone_number()[:15],
        is_celebrity=is_celebrity
    )

def generate_people(n, existing_personnummers):
    """En generator som genererar n antal personer."""
    # Generera 10% kändisar
    for _ in range(int(n * 0.1)):
        yield generate_person(existing_personnummers, is_celebrity=True)
    # Generera resterande vanliga personer
    for _ in range(n - int(n * 0.1)):
        yield generate_person(existing_personnummers)

def seed_database(n=1000000, batch_size=100000):
    """Skapar och sparar n antal personer i databasen i batcher."""
    total_seeded = 0
    
    # Ladda alla existerande personnummer från databasen för att undvika duplicater
    existing_personnummers = set(p[0] for p in db.session.query(Person.personnummer).all())
    people_gen = generate_people(n, existing_personnummers)
    
    start_time = time.time()  # Starta tidtagning

    while total_seeded < n:
        try:
            batch = [next(people_gen) for _ in range(min(batch_size, n - total_seeded))]
            db.session.bulk_save_objects(batch)
            db.session.commit()
            total_seeded += len(batch)
            batch_time = time.time()  # Tid efter varje batch
            print(f"Seedade {total_seeded} personer hittills... Tid för denna batch: {batch_time - start_time:.2f} sekunder.")
            start_time = batch_time  # Uppdatera starttid för nästa batch
        except IntegrityError as e:
            db.session.rollback()
            print(f"IntegrityError vid seedning av batch {total_seeded // batch_size + 1}: {e}")
            # Här kan du implementera logik för att hantera duplicater, t.ex. regenerera vissa poster
            # För enkelhetens skull, här stoppar vi processen
            break
    
    print(f"Totalt seedade {total_seeded} personer till databasen.")

def clear_table():
    """Tömmer Person-tabellen."""
    db.session.query(Person).delete()
    db.session.commit()
