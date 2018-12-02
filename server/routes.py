"""
Author: Mariia Shatalova (radeon4650main@gmail.com)
"""

from flask import render_template
from . import app, Employee


@app.route('/')
def main():
    empls = Employee.query.filter(Employee.chief == Employee.id).all()
    return render_template('table_template.html', employees=empls, chief_id='undef')

@app.route('/subordinates/<userid>')
def get_subordinates(userid):
    subordinates = Employee.query.filter(Employee.chief == userid).filter(Employee.id != userid).all()
    return render_template('list_element_template.html', employees=subordinates, chief_id=userid)