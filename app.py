from flask import Flask
from config import DATABASE_CONNECTION_URI

from routes.burgas import burgas

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = "secret key"

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI

SQLAlchemy(app)


app.register_blueprint(burgas)