"""
Author: Mariia Shatalova (radeon4650main@gmail.com)
"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, UnicodeText, DateTime

db = SQLAlchemy()

class Employee(db.Model):
    __tablename__ = 'employees'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)

    username = Column(UnicodeText(40), nullable=False, unique=False)
    position = Column(UnicodeText(40), nullable=False, unique=False)
    employment_date = Column(DateTime, nullable=False, unique=False)
    salary = Column(Integer, nullable=False, unique=False)
    chief = Column(Integer, nullable=False, unique=False)

    login = Column(UnicodeText(40), unique=True)
    pwd = Column(UnicodeText(80), nullable=False, unique=False)

    user_pic = Column(UnicodeText, nullable=True, unique=False)

    def __repr__(self):
        return '<Employee %r>' % self.username