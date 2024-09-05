 #Innehåller definitionerna av applikationens rutter (de URL
# som användarna kan besöka).
# Här specificerar du vad som ska hända när en användare går till en specifik URL, till exempel att rendera en HTML-sida eller interagera med databasen.
# routes.py

# routes.py
from flask import Blueprint, render_template, request
from app.lru_cache import lru_cache  # Importerar din LRU-cache
from app.models import Person, db
import time
from sqlalchemy.sql.expression import func  # För random sortering

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return render_template('home.html')

@routes.route('/index')
def index():
    # Hämta alla parametrar från URL
    page = request.args.get('page', 1, type=int)
    prev_page = request.args.get('prev_page', None)
    search_query = request.args.get('search', '')
    sort_by = request.args.get('sort_by', 'random')
    sort_order = request.args.get('sort_order', 'none')
    filter_celebs = request.args.get('filter_celebs', 'no')

    query = Person.query

    # Filtrering för sökning
    if search_query:
        query = query.filter(
            (Person.name.like(f'%{search_query}%')) |
            (Person.personnummer.like(f'%{search_query}%')) |
            (Person.city.like(f'%{search_query}%')) |
            (Person.profession.like(f'%{search_query}%')) |
            (Person.phone_number.like(f'%{search_query}%'))
        )

    # Hantering av kändisfilter och sortering
    if filter_celebs == 'yes':
        # Om användaren vill visa kändisar först
        query = query.order_by(Person.is_celebrity.desc())
        if sort_by == 'random':
            query = query.order_by(func.random())  # Blandar återstående personer
        elif sort_order != 'none':
            if sort_order == 'asc':
                query = query.order_by(getattr(Person, sort_by).asc())
            elif sort_order == 'desc':
                query = query.order_by(getattr(Person, sort_by).desc())
    else:
        # Om ingen kändisfilter valts, använd vanlig sortering
        if sort_by == 'random':
            query = query.order_by(func.random())  # Slumpmässig ordning
        elif sort_order != 'none':
            if sort_order == 'asc':
                query = query.order_by(getattr(Person, sort_by).asc())
            elif sort_order == 'desc':
                query = query.order_by(getattr(Person, sort_by).desc())

    # Paginering
    pagination = query.paginate(page=page, per_page=20, error_out=False)
    people = pagination.items

    # Skicka tillbaka alla sök- och filterparametrar till index.html
    return render_template(
        'index.html', 
        people=people, 
        pagination=pagination, 
        prev_page=prev_page, 
        search_query=search_query, 
        sort_by=sort_by, 
        sort_order=sort_order, 
        filter_celebs=filter_celebs
    )

@routes.route('/person/<int:id>')
def person(id):
    # Hämta alla parametrar för att behålla dem när man återvänder till listan
    prev_page = request.args.get('prev_page', None)
    search_query = request.args.get('search_query', '')
    sort_by = request.args.get('sort_by', 'random')
    sort_order = request.args.get('sort_order', 'none')
    filter_celebs = request.args.get('filter_celebs', 'no')
    
    person = lru_cache.get(id)
    if person is None:
        print(f"Hämtar från databasen: Person ID {id}")
        time.sleep(5)  # Simulerar långsam databasförfrågan
        person = Person.query.get_or_404(id)
        lru_cache.put(id, person)  # Lägg till personen i cachen
    else:
        print(f"Hämtar från cachen: Person ID {id}")

    # Skicka tillbaka alla parametrar för att kunna behålla dem när man går tillbaka
    return render_template(
        'person.html', 
        person=person, 
        prev_page=prev_page,
        search_query=search_query,
        sort_by=sort_by,
        sort_order=sort_order,
        filter_celebs=filter_celebs
    )

