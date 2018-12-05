"""
Author: Mariia Shatalova (radeon4650main@gmail.com)
"""

from server import engine, app, Employee
from faker import Faker
from sqlalchemy import exc

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


def add_random_employees(count=1, chief=None):
    with app.app_context():
        for i in range(count):
            added = False
            while not added:
                try:
                    employee = create_random_employee(chief)
                    engine.session.add(employee)
                    engine.session.commit()
                    added = True
                except exc.DataError:
                    engine.session.rollback()
                    added = False
                except exc.IntegrityError:
                    engine.session.rollback()
                    added = False


def get_test_employees(count=None):
    with app.app_context():
        if count is None:
            return Employee.query.all()
        else:
            return Employee.query.limit(count).all()


if __name__ == '__main__':
    print("starting...")

    shift = 1
    for i in range(1, 11):
        add_random_employees(count=1, chief=i)

    for i in range(5):
        for e in get_test_employees():
            if shift > e.id: continue
            shift = e.id
            add_random_employees(count=10, chief=shift)
        shift += 1

    # for e in get_test_employees():
    #     print(e.id)