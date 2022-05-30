from random import sample
from flask import Flask, render_template, request
from importlib_metadata import NullFinder
import csv
import sys

sys.path.append("../Backend")
from datasource import *

app = Flask(__name__)
database = DataSource()

@app.route('/')
def homepage():
    """ Generate a homepage
    @return a homepage with instructions
    """ 
    return render_template('homepage.html', productList=database.get_products_list(), brandList=database.get_brand_list())

@app.route('/contact')
def contact():
    """ Generate a contact page
    """
    return render_template('contact.html')

@app.route('/help')
def help():
    """ Generate a help page
    """
    return render_template('help.html')

@app.route('/contact/contact_submitted')
def contact_submitted():
    """ Let users submit a contact form
    """
    return render_template('contact_submitted.html')
    
@app.route('/displayproducts', methods=['POST'])
def display_products():
    """ Generate a page that displays ingredients
    @return a page with a list of all products carried by the brand
    """ 
    brand = (request.form['brandSearch'])
    return render_template('products.html', brand=brand, products=database.get_all_products_from_brand(brand))

@app.route('/displayingredients', methods=['POST'])
def display_ingredients():
    """ Generate a page that returns ingredients
    @return a page with a list of all ingredients of the product
    """ 
    product = (request.form['product'])
    return render_template('ingredients.html', product=product, ingredients=database.get_all_ingredients_from_product(product))

@app.errorhandler(404)
def page_not_found(e):
    """ Generate a page that returns ingredients
    @param 
        e: 404 error
    @return an error statement
    """ 
    return render_template('error.html')

@app.errorhandler(500)
def python_bug(e):
    """ Generate a page that returns ingredients
    @param 
        e: 500 error
    @return an error statement
    """ 
    return render_template('error.html')

if __name__ == '__main__':
    # app.run()
    app.run(host='0.0.0.0', port=5112)
