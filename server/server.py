"""
Author: Mariia Shatalova (radeon4650main@gmail.com)
"""

from flask import Flask
from flask import render_template
from db import engine, Employee
from sqlalchemy.orm import sessionmaker


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

@app.route('/')
def main():
    empls = Employee.query.all()
    return render_template('table_template.html', employees=empls)

if __name__ == '__main__':
    app.run()
