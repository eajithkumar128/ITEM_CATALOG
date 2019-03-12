from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
app = Flask(__name__)


from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from models import Base, Category, Items
from sqlalchemy import desc


import datetime

engine = create_engine('sqlite:///itemcatalogdb.db',
						connect_args={'check_same_thread':False})
Base.metadata.bind = engine


DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route("/")
@app.route("/catalog")
def homePage():
	category = session.query(Category).all()
	# items = session.query(Items).order_by(id)
	items = session.query(Items).order_by(desc(Items.upload_date))
	return render_template('homePage.html',category=category,items=items)


@app.route("/catalog/<string:category>/items")
def catalogItems(category):
	return "specific items catalog"


@app.route("/catalog/<string:category>/<string:item>/")
def itemDetails(category,item):
	return "items descirption"


@app.route("/catalog/add/items",methods=['GET','POST'])
def addItem():
	if request.method == 'POST':
		newItem = Items(title=request.form['name'],
							Description=request.form['description'],
							Category_name = request.form['category_name'],
							upload_date=datetime.datetime.now())
		session.add(newItem)
		session.commit()
		return redirect(url_for('homePage'))
	else:
		category = session.query(Category).all()
		return render_template('newItem.html',category=category)


if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0',port=5000)
