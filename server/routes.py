# -*- coding: utf-8 -*-
"""
Copyright © 2018 abz.agency.test_task. All rights reserved.
Author: Mariia Shatalova (radeon4650main@gmail.com)
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
     http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from flask import render_template, redirect, request, url_for, flash, session, g
from . import app, Employee, engine
import functools


@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        if username != 'admin':
            error = 'Incorrect username.'
        elif password != '1234':
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user'] = username
            return redirect(url_for('get_list'))

        flash(error)
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(*args, **kwargs):
        if not session.get('user'):
            return redirect(url_for('login'))

        return view(*args, **kwargs)
    return wrapped_view


@app.route('/')
def main():
    empls = Employee.query.filter(Employee.chief == Employee.id).all()
    return render_template('table_template.html', employees=empls, chief_id='undef')


@app.route('/list/')
@login_required
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