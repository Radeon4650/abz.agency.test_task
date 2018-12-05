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

from datetime import datetime
from sqlalchemy import Column, Integer, DateTime, VARCHAR, UnicodeText

from . import engine

class Employee(engine.Model):
    __tablename__ = 'employees'
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)

    username = Column(VARCHAR(40), nullable=False, unique=False)
    position = Column(VARCHAR(40), nullable=False, unique=False)
    employment_date = Column(DateTime, nullable=False, unique=False)
    salary = Column(Integer, nullable=False, unique=False)
    chief = Column(Integer, nullable=False, unique=False)

    login = Column(VARCHAR(40), nullable=False, unique=True)
    pwd = Column(VARCHAR(80), nullable=False, unique=False)

    user_pic = Column(VARCHAR(255), nullable=True, unique=False)

    def get_date_str(self):
        return self.employment_date.strftime("%Y-%m-%d")
    def __repr__(self):
        return '<Employee %r>' % self.username