from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime
from os import path
import os

app = Flask(__name__);
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///main.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
app.secret_key = "Cyberpunk2023";

db = SQLAlchemy(app);
app.app_context().push();

from App import routes
from App.models import UserModel

def create_database():
	if not path.exists('App/main.db'):
		db.create_all();
		

create_database();