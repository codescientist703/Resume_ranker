from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c6275dd74b8478932e00973af22d2919'
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

from flasksite import routes