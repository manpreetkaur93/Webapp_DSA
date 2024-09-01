#filen innehåller alla inställningar och konfigurationer för din Flask-applikation, såsom databasuppkopplingar och API-nycklar.

#Exempel på inställningar:
# SECRET_KEY: Används av Flask för säkerhetsfunktioner, såsom sessionshantering.
# SQLALCHEMY_DATABASE_URI: Här ställer du in din databasanslutning.
import os

class Config:
    SECRET_KEY = 'someverysecretkeyhere'
    SQLALCHEMY_DATABASE_URI ="mysql+mysqlconnector://root:password@localhost:3306/person_data"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
   
