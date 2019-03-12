import os
import sys
from sqlalchemy import Column, ForeignKey, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()


class Category(Base):
	__tablename__ = 'category'

	id = Column(Integer,primary_key=True)
	name = Column(String(30),nullable=False)


class Items(Base):
	__tablename__ = 'items'

	id = Column(Integer,primary_key=True)
	title = Column(String(30),nullable=False)
	Description = Column(String(250))
	Category_name = Column(String(30),nullable=False)
	upload_date = Column(DateTime,nullable=False)


engine = create_engine('sqlite:///itemcatalogdb.db')


Base.metadata.create_all(engine)
