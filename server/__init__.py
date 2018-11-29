"""
Author: Mariia Shatalova (radeon4650main@gmail.com)
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('table_template.html')


if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run()