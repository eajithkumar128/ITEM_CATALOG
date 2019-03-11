import os
import sys
from sqlalchemy import Column, ForeignKey, String, Integer
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
	Category_id = Column(Integer, ForeignKey('category.id'))
	category = relationship(Category)


engine = create_engine('sqlite:///itemcatalog.db')


Base.metadata.create_all(engine)