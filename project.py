from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
app = Flask(__name__)


from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from modelsNew import Base, Category, Items
from sqlalchemy import desc


import datetime

engine = create_engine('sqlite:///itemcategory.db',
						connect_args={'check_same_thread':False})
Base.metadata.bind = engine


DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route("/")
@app.route("/catalog")
def homePage():
	category = session.query(Category).all()
	items = session.query(Items).order_by(desc(Items.upload_date)).all()
	return render_template('homePage.html',category=category,items=items)


@app.route("/catalog/<int:category_id>/items")
def catalogItems(category_id):
	categoryItems = session.query(Items).filter_by(
							category_id=category_id).all()
	category = session.query(Category).filter_by(
							id=category_id
						).one()
	allCategory= session.query(Category).all()
	return render_template('catalogItem.html',
								Category_name=category,
								category=allCategory,
								categoryItems=categoryItems)


@app.route("/catalog/new",methods=['GET','POST'])
def addCategory():
	if request.method == 'POST':
		newCategory = Category(name=request.form['name'])
		session.add(newCategory)
		session.commit()
		return redirect(url_for('homePage'))
	else:
		return render_template('newCategory.html')


@app.route("/catalog/<int:category_id>/edit/",methods=['GET','POST'])
def editCategory(category_id):
	editedCategory = session.query(Category).filter_by(id=category_id).one()
	if request.method == 'POST':
	    if request.form['name']:
	    	editedCategory.name = request.form['name']
	    session.add(editedCategory)
	    session.commit()
	    return redirect(url_for('homePage'))
	else:
		return render_template('editCategory.html',category=editedCategory)


@app.route("/catalog/<int:category_id>/delete/",methods=['GET','POST'])
def deleteCategory(category_id):
	deleteCategory = session.query(Category).filter_by(id=category_id).one()
	if request.method == 'POST':
		session.delete(deleteCategory)
		session.commit()
		return redirect(url_for('homePage'))
	else:
		return render_template('deleteCategory.html',category=deleteCategory)


@app.route("/catalog/<int:category_id>/<int:item>/")
def itemDetails(category_id,item):
	itemDetail = session.query(Items).filter_by(id=item).one()
	return render_template('itemDetail.html',itemDetail=itemDetail)


@app.route("/catalog/add/items",methods=['GET','POST'])
def addItem():
	if request.method == 'POST':
		category = session.query(Category).filter_by(id=request.form['category_id'])
		newItem = Items(title=request.form['name'],
							Description=request.form['description'],
							upload_date=datetime.datetime.now(),
							category=category)
		session.add(newItem)
		session.commit()
		return redirect(url_for('homePage'))
	else:
		category = session.query(Category).all()
		return render_template('newItem.html',category=category)


@app.route("/catalog/<int:category_id>/<int:item_id>/edit",methods=['GET','POST'])
def editItem(category_id,item_id):
	editedItem = session.query(Items).filter_by(id=item_id).one()
	if request.method == 'POST':
	   if request.form['name']:
	   		editedItem.title=request.form['name']
	   if request.form['Description']:
	   		editedItem.Description = request.form['Description']
	   session.add(editedItem)
	   session.commit()
	   return redirect(url_for('itemDetails',category_id=category_id,item=editedItem.id))
	else:
		category = session.query(Category).all()
		itemDetail = session.query(Items).filter_by(id=item_id).one()
		return render_template('editItem.html',item=itemDetail,category=category)


@app.route("/catalog/<int:category_id>/<int:item_id>/delete",methods=['GET','POST'])
def deleteItem(category_id,item_id):
	category = session.query(Category).filter_by(id=category_id).one()
	itemToDelete = session.query(Items).filter_by(id=item_id).one()
	if request.method == 'POST':
	   session.delete(itemToDelete)
	   session.commit()
	   return redirect(url_for('catalogItems',category=category.name))
	else:
		itemDetail = session.query(Items).filter_by(id=item_id).one()
		return render_template('deleteItem.html',item=itemDetail)


if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0',port=5000)
