# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request, redirect
from datetime import datetime
from model import getImageUrlFrom
from flask_pymongo import PyMongo
import os
from bson.objectid import ObjectId

# -- Initialization section --
app = Flask(__name__)

app.config['MONGO_DBNAME'] = os.getenv('DBNAME')
dbname = app.config['MONGO_DBNAME']    
app.config['USER'] = os.getenv('DBUSER')
user = app.config['USER']    
app.config['MONGO_PWD'] = os.getenv('DBPWD')   
pwd = app.config['MONGO_PWD']    

is_prod = os.environ.get('IS_HEROKU', None)
if is_prod:
    dbname = os.environ.get('DBNAME')
    user = os.environ.get('DBUSER')
    pwd = os.environ.get('DBPWD')
# URI of database   
app.config['MONGO_URI'] = f"mongodb+srv://{user}:{pwd}@cluster0.seola.mongodb.net/{dbname}?retryWrites=true&w=majority"
mongo = PyMongo(app)

# -- Routes section --
@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template("homepage.html", time = datetime.now())
@app.route('/about')
def about():
    return render_template("about.html", time = datetime.now())

# @app.route('/profile')
# def profile():
#     return render_template("profile.html", time=datetime.now())

# @app.route('/login')
# def login():
#     return "This is a placeholder for the login page"

# @app.route('/sign-up')
# def signup():
#     return "This is a placeholder for the sign-up page"

# @app.route('/shopping', methods = ['GET', 'POST'])
# def shopping():
#     print(request.form)
#     nickname = request.form['nickname']
#     return redirect('/shopping/'+nickname)

# @app.route('/shopping/<nickname>')
# def shopping_s(nickname):
#     return "Got your nickname, which is "+nickname

# @app.route('/submit/diy')
# def s_d():
#     return "This is a placeholder for a page to submit diy's"


# @app.route('/browse/diy')
# def b_d():
#     return "This is a placeholder for the diy exploring page"


@app.route('/submit/products')
def s_p():
    return render_template("submit_product.html", time=datetime.now())

@app.route('/submit/complete', methods = ['GET', 'POST'])
def s_c():
    if request.method == "GET":
        return "Error! You didn't put in a product."
    else:
       print(request.form)
       product_name = request.form['product_name']
       img_url = request.form['product_image_url']
       user = request.form['user']
       product_url = request.form['product_url']
       category = request.form['category']

       # get the collection you want to use
       collection = mongo.db.products
       # insert the new data
       new_product = {'product': product_name, 'img': img_url, 'user': user, 'url': product_url, 'category': category}
       collection.insert(new_product)
       return "Thanks for your submission"

@app.route('/browse/products')
def b_p():
    collection = mongo.db.products
    products = collection.find({})
    return render_template('browse_products.html', products=products)

@app.route('/browse/products/<product_id>')
def spec_p(product_id):
    collection = mongo.db.products
    product = collection.findOne({'_id': ObjectId(product_id)})
    return render_template("specific_recipe.html", product = product)

# @app.route('/search', methods = ['GET', 'POST'])
# def search_handle():
#     if request.method == "GET":
#         return "Error! You didn't put anything in the search bar."
#     else: 
#        print(request.form)
#        search = request.form['search']
#        redirect('/search/'+search)

# @app.route('/search/<search>')
# def search():
#     collection = mongo.db.products
#     products = collection.find({"product" : {'$regex' : '.*' + search + '.*i'}})
#     if products.count() == 0:
#         return "No elements match your query"
#     else:
#         return render_template('/')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

# @app.route('/add/diy')
# def add_d():
#     return "This is a placeholder for the method for submitting a diy"

# @app.route('/add/product')
# def add_p():
#     return "This is a placeholder for the method for submitting a product"