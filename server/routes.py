"""
Author: Mariia Shatalova (radeon4650main@gmail.com)
"""

from flask import render_template, redirect, request
from . import app, Employee, engine


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


@app.route("/list/delete/id=<id>", methods=["POST"])
def delete(id):
    print ('Delete:', id)
    # setting new chief to subordinates
    todel = Employee.query.filter(Employee.id == id).first()
    chief = todel.chief
    if chief == id:
        for empl in Employee.query.filter(Employee.chief==id).all():
            empl.chief = empl.id
    else:
        for empl in Employee.query.filter(Employee.chief==id).all():
            empl.chief = chief
    # deleting record
    engine.session.delete(todel)
    engine.session.commit()
    return redirect("/list/")


@app.route("/list/update/id=<id>", methods=["GET", "POST"])
def update(id):
    print('Update:', id)
    e = Employee.query.filter(Employee.id == id).first()
    if request.method == 'GET':
        return render_template('create_update_dialog_template.html', employee=e)
    else:
        e.username = request.form['username']
        e.position = request.form['position']
        e.employment_date = request.form['employment_date']
        e.salary = request.form['salary']
        e.chief = request.form['chief']
        e.login = request.form['login']
        e.pwd = request.form['pwd']
        engine.session.commit()
        return redirect("/list/")


@app.route("/list/create/", methods=["POST"])
def create():
    print ('Create...')
    new_user = Employee(username=request.form['username'],
        position=request.form['position'],
        employment_date=request.form['employment_date'],
        salary=request.form['salary'],
        chief=request.form['chief'],
        login=request.form['login'],
        pwd=request.form['pwd'])
    engine.session.add(new_user)
    engine.session.commit()
    return redirect("/list/")


@app.route('/subordinates/<userid>')
def get_subordinates(userid):
    subordinates = Employee.query.filter(Employee.chief == userid).filter(Employee.id != userid).all()
    return render_template('list_element_template.html', employees=subordinates, chief_id=userid)