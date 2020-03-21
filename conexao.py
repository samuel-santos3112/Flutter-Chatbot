# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql://postgres:psql@localhost:5432/cadastro')
Session = sessionmaker(bind=engine)

session = Session()
Base = declarative_base()
