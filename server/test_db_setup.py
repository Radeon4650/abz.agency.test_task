"""
Author: Mariia Shatalova (radeon4650main@gmail.com)
"""

from faker import Faker

from db import Session, init_test_db, Employee

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



def add_random_employees(count=1):
    session = Session()
    for i in range(count):
        employee = create_random_employee()
        session.add(employee)
    session.commit()

def get_test_employees(count=None):
    session = Session()
    if count is None:
        return session.query(Employee).all()
    else:
        return session.query(Employee).limit(count).all()


if __name__ == '__main__':
    print("starting...")
    # init_test_db()
    add_random_employees(100)
    for e in get_test_employees():
        print(e.username)