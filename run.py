#run.py är den fil som används för att starta Flask-applikationen.
from app.models import clear_table, db, seed_database, Person
from app import app

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # Kontrollera om det redan finns data innan du seedar
        if Person.query.count() == 0:
            seed_database(10000)  # Seeda databasen om den är tom
    app.run(debug=True)
