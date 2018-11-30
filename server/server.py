"""
Author: Mariia Shatalova (radeon4650main@gmail.com)
"""

from flask import render_template
from . import app, Employee

@app.route('/')
def main():
    empls = Employee.query.all()
    return render_template('table_template.html', employees=empls)

if __name__ == '__main__':
    app.run()
