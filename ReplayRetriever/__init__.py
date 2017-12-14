"""A module providing a Flask interface for the display
and retrieval of meta data about dota 2 replays.
Provides the information required to filter and download replays.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from ReplayRetriever import models
