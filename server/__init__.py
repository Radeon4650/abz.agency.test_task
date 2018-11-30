from flask import Flask

from .db import engine, Employee
app = Flask(__name__)
POSTGRES = {
        'user': 'postgres',
        'pw': 'password',
        'db': 'test_db',
        'host': 'localhost',
        'port': '5432',
    }
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
engine.init_app(app)

from .routes import *