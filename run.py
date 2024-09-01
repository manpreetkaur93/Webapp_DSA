#run.py är den fil som används för att starta Flask-applikationen.
from app.models import clear_table, db, seed_database 

from app import app
#sys.path.insert(0, '/path/to/Webapp_DSA')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        clear_table()
        seed_database(10000)
    app.run(debug=True)
  