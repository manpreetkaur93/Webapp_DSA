# '''Denna fil används för att initiera din Flask-applikation.
# Här importeras nödvändiga moduler, laddas konfigurationer och sätts upp rutter (webbsidorna som användarna kan navigera till).'''
# __init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .routes import routes  # Använd relativ import
from .models import db, seed_database  # Använd relativ import

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(routes)

