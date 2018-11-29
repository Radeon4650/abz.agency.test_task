"""
Author: Mariia Shatalova (radeon4650main@gmail.com)
"""
from sqlalchemy import Column, Integer, DateTime, VARCHAR, UnicodeText

from db import engine


class Employee(engine.Model):
    __tablename__ = 'employees'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)

    username = Column(VARCHAR(40), nullable=False, unique=False)
    position = Column(VARCHAR(40), nullable=False, unique=False)
    employment_date = Column(DateTime, nullable=False, unique=False)
    salary = Column(Integer, nullable=False, unique=False)
    chief = Column(Integer, nullable=False, unique=False)

    login = Column(VARCHAR(40), unique=True)
    pwd = Column(VARCHAR(80), nullable=False, unique=False)

    user_pic = Column(VARCHAR(255), nullable=True, unique=False)

    def __repr__(self):
        return '<Employee %r>' % self.username