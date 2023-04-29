from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import join_room, leave_room, send, SocketIO
import datetime
from os import path
import os


app = Flask(__name__);
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///main.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "Cyberpunk2023";
socketio = SocketIO(app);

db = SQLAlchemy(app);
app.app_context().push();

from App import routes
from App.models import UserModel

def create_database():
	if not path.exists('App/main.db'):
		db.create_all();
		

create_database();
if __name__ == "__main__":
	socketio.run(app);
	