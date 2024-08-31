 #Innehåller definitionerna av applikationens rutter (de URL
# som användarna kan besöka).
# Här specificerar du vad som ska hända när en användare går till en specifik URL, till exempel att rendera en HTML-sida eller interagera med databasen.
# routes.py

# routes.py
from flask import Blueprint, render_template, request
from app.lru_cache import lru_cache

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    # Din logik här
    return render_template('index.html')

@routes.route('/person/<int:id>')
def person(id):
    # Din logik här
    return f"Person with id {id}"
