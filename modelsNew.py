import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()

class Category(Base):
    __tablename__ = 'category'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

 
class Items(Base):
    __tablename__ = 'items'


    title =Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    Description = Column(String(250))
    upload_date = Column(DateTime,nullable=False) 	
    category_id = Column(Integer,ForeignKey('category.id'))
    category = relationship(Category)


engine = create_engine('sqlite:///itemcategory.db')
 

Base.metadata.create_all(engine)