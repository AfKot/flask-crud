from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from task import app
#from task import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

db = SQLAlchemy(app)

from application import routes