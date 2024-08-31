'''Denna fil används för att initiera din Flask-applikation.
Här importeras nödvändiga moduler, laddas konfigurationer och sätts upp rutter (webbsidorna som användarna kan navigera till).'''
# __init__.py
from flask import Flask
from .routes import routes

app = Flask(__name__)
app.config.from_pyfile('../config.py')  # Går upp en nivå för att hitta config.py

app.register_blueprint(routes)  # Registrera din Blueprint

if __name__ == '__main__':
    app.run(debug=True)


