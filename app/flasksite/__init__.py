from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os.path


app = Flask(__name__)
app.config['SECRET_KEY'] = 'c6275dd74b8478932e00973af22d2919'
app.config['SQLALCHEMY_DATABASE_URL'] ='sqlite://site.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from flasksite import routes