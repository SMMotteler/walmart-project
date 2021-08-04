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

@app.route('/profile')
def profile():
    return render_template("profile.html", time=datetime.now())

@app.route('/login')
def login():
    return "This is a placeholder for the login page"

@app.route('/sign-up')
def signup():
    return "This is a placeholder for the sign-up page"

# @app.route('/shopping', methods = ['GET', 'POST'])
# def shopping():
#     print(request.form)
#     nickname = request.form['nickname']
#     return redirect('/shopping/'+nickname)

# @app.route('/shopping/<nickname>')
# def shopping_s(nickname):
#     return "Got your nickname, which is "+nickname

@app.route('/submit/diy')
def s_d():
    return "This is a placeholder for a page to submit diy's"


@app.route('/browse/diy')
def b_d():
    return "This is a placeholder for the diy exploring page"


@app.route('/submit/products')
def s_p():
    return "This is a placeholder for a page to submit products"

@app.route('/browse/products')
def b_p():
    return "This is a placeholder for the product exploring page"

@app.route('/search')
def search():
    return "This is a placeholder for a page to show a results of a search"

@app.route('/add/diy')
def add_d():
    return "This is a placeholder for the method for submitting a diy"

@app.route('/add/product')
def add_p():
    return "This is a placeholder for the method for submitting a product"