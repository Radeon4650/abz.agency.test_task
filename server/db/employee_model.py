"""
Author: Mariia Shatalova (radeon4650main@gmail.com)
"""

from sqlalchemy import Column, Integer, UnicodeText, DateTime

# from . import BASE_MODEL


class Employee(BASE_MODEL):
    __tablename__ = 'employees'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)

    username = Column(UnicodeText(40), nullable=False, unique=False)
    position = Column(UnicodeText(40), nullable=False, unique=False)
    employment_date = Column(DateTime, nullable=False, unique=False)
    salary = Column(Integer, nullable=False, unique=False)

    # login = Column(UnicodeText(40), unique=True)
    # pwd_hash = Column(UnicodeText(80), nullable=False, unique=False)

    # user_pic = Column(UnicodeText, nullable=True, unique=False)