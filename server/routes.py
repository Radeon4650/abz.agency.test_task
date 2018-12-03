"""
Author: Mariia Shatalova (radeon4650main@gmail.com)
"""

from flask import render_template
from . import app, Employee


@app.route('/')
def main():
    empls = Employee.query.filter(Employee.chief == Employee.id).all()
    return render_template('table_template.html', employees=empls, chief_id='undef')


@app.route('/list/')
def get_list():
    limit = 100
    empls = Employee.query.order_by(Employee.username).limit(limit).all()
    return render_template('general_list.html', employees=empls)



@app.route('/list/gen_list_cont/offset=<offset>&quantity=<quantity>&order_by=<order>')
def get_gen_list_content(offset, quantity, order):
    empls = Employee.query.order_by(order).offset(offset).limit(quantity).all()
    return render_template('general_list_content.html', employees=empls)


@app.route('/list/search/field=<field>&value=<value>')
def search_by(field, value):
    empls = Employee.query.filter(getattr(Employee, field)==value).all()
    return render_template('general_list_content.html', employees=empls)


@app.route('/subordinates/<userid>')
def get_subordinates(userid):
    subordinates = Employee.query.filter(Employee.chief == userid).filter(Employee.id != userid).all()
    return render_template('list_element_template.html', employees=subordinates, chief_id=userid)