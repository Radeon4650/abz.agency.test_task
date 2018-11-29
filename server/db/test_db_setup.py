"""
Author: Mariia Shatalova (radeon4650main@gmail.com)
"""

from faker import Faker
from .employee_model import db, Employee

fake = Faker('ru_RU')


def create_random_employee(chief=None):
    username = fake.name()
    position = fake.job()
    employment_date = fake.date_this_decade(before_today=True)
    salary = fake.random.randint(5000, 50000)
    if chief is None:
        chief = fake.random.randint(0, 50000)

    login = fake.user_name()
    pwd = fake.password()
    user_pic = fake.image_url()

    return Employee(username=username, position=position, employment_date=employment_date, salary=salary,
                    chief=chief, login=login, pwd=pwd, user_pic=user_pic)


def init_test_db(app):
    db.create_all()


def add_random_employees(app, count=1):
    db.init_app(app)
    for i in range(count):
        employee = create_random_employee()
        db.session.add(employee)
    db.session.commit()

def get_test_employees(app, count=None):
    if count is None:
        return Employee.query.all()
    else:
        return Employee.query.limit(count).all()
