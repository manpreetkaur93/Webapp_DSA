import os

class Config:
    SECRET_KEY = 'someverysecretkeyhere'
    SQLALCHEMY_DATABASE_URI ="mysql+mysqlconnector://root:password@localhost:3306/person_data"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
   
