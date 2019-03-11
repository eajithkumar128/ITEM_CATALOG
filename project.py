from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
app = Flask(__name__)


from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from models import Base, Category, Items


engine = create_engine('sqlite:///itemcatalog.db',
						connect_args={'check_same_thread':False})
Base.metadata.bind = engine


DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route("/")
@app.route("/catalog")
def homePage():
	category = session.query(Category).all()
	items = session.query(Items).all()
	return render_template('homePage.html',category=category,items=items)


@app.route("/catalog/<string:category>/items")
def catalogItems(category):
	return "specific items catalog"


@app.route("/catalog/<string:category>/<string:item>/")
def itemDetails(category,item):
	return "items descirption"


@app.route("/catalog/add/items")
def addItem():
	return render_template('newItem.html')


if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0',port=5000)