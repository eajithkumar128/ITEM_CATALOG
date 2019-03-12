from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Category, Base, Items

import datetime


currentDT = datetime.datetime.now()

engine = create_engine('sqlite:///itemcatalogdb.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

session.query(Category).delete()
session.commit()

#Menu for UrbanBurger
category1 = Category(name = "Football")

session.add(category1)
session.commit()

category2 = Category(name = "Hockey")

session.add(category2)
session.commit()


Item1 = Items(title='ball',Description='something about the ball',Category_name="Football",upload_date=datetime.datetime.now())

session.add(Item1)
session.commit()


Item2 = Items(title='Shoe',Description='something about the shoe',Category_name="Hockey",upload_date=datetime.datetime.now())

session.add(Item2)
session.commit()
