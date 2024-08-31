#run.py är den fil som används för att starta Flask-applikationen.


from app import app

if __name__ == "__main__":
    app.run(debug=True)