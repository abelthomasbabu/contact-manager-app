from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # To send cross origin requests to our app

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db" # Specifying the local db
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # Not tracking modifications to db

db = SQLAlchemy(app) # Instance of db to access the db to CRUD [Acts as an ORM]