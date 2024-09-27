from app.models import db, seed_database, Person
from app import app

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        #clear_table()  # Töm databasen om man vill börja om
        #seed_database(1000000, batch_size=100000)  # Seeda 1 miljon personer i batchar
    app.run(debug=True)


