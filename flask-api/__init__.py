#__init__.py
from flask import Flask
from flask.sqlalchemy import SQLAlchemy
from config import Config
from . import views

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)