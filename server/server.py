"""
Author: Mariia Shatalova (radeon4650main@gmail.com)
"""

from flask import Flask
from flask import render_template


app = Flask(__name__)
POSTGRES = {
        'user': 'postgres',
        'pw': 'password',
        'db': 'test_db',
        'host': 'localhost',
        'port': '5432',
    }
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

@app.route('/')
def main():
    return render_template('table_template.html')


if __name__ == '__main__':
    app.run()
