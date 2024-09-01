 #Innehåller definitionerna av applikationens rutter (de URL
# som användarna kan besöka).
# Här specificerar du vad som ska hända när en användare går till en specifik URL, till exempel att rendera en HTML-sida eller interagera med databasen.
# routes.py

# routes.py
from flask import Blueprint, render_template, request
from app.lru_cache import lru_cache  # Importerar din LRU-cache
from app.model import Person
import time

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    people = Person.query.paginate(page=page, per_page=20)
    return render_template('index.html', people=people.items, pagination=people)

@routes.route('/person/<int:id>')
def person(id):
    person = lru_cache.get(id)
    if person is None:
        # Simulerar långsam databasförfrågan med en fördröjning
        time.sleep(5)
        person = Person.query.get_or_404(id)
        lru_cache.put(id, person)  # Lägg till personen i cachen
    return render_template('person.html', person=person)
