from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


POSTGRES = {
        'user': 'postgres',
        # 'pw': 'password',
        'db': 'test_db',
        'host': 'localhost',
        'port': '5432',
    }
# postgresql+psycopg2://user:password@hostname/database_name
# db_string = 'postgresql://%(user)s:\%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
db_string = 'postgresql://%(user)s@%(host)s:%(port)s/%(db)s' % POSTGRES
engine = create_engine(db_string)
base = declarative_base()
Session = sessionmaker(engine)

# from test_db_setup import base
from .employee_model import Employee

def init_test_db():
    # session = Session()
    base.metadata.create_all(engine)
