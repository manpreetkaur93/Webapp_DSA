# Webapp_DSA
## Beskrivning
Denna webbapplikation är utvecklad i [Flask] och använder MySQL för att hantera en databas med 1 000 000 personer. Applikationen demonstrerar användningen av en LRU (Least Recently Used) cache för att effektivisera åtkomst till de mest efterfrågade personuppgifterna.

## Funktioner
- Databas Seeding: Initialt seedas databasen med 1 000 000 personuppgifter inklusive namn, personnummer, stad, och andra relevanta uppgifter.
- Pagination: Visar en lista på 20 personer per sida med namn och stad.
- Detaljerad Vy: Klicka på en person för att se detaljerade uppgifter, där data hämtas från en LRU-cache för att snabba upp åtkomsten.

## Tekniska Krav
- Flask
- MySQL
- Python 

## Installation
1. Klona repo: `gh repo clone manpreetkaur93/Webapp_DSA`
2. Installera beroenden: `pip install -r requirements.txt`
3. Starta applikationen: `python run.py`

## Användning
Starta servern och navigera till `localhost:5000` för att interagera med applikationen.



