'''Denna fil används för att initiera din Flask-applikation.
Här importeras nödvändiga moduler, laddas konfigurationer och sätts upp rutter (webbsidorna som användarna kan navigera till).'''
# __init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.routes import routes
from app.model import db

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)
migrate = Migrate(app, db)  # Initialisera Flask-Migrate

app.register_blueprint(routes)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Skapa alla tabeller om de inte redan finns
    app.run(debug=True)
