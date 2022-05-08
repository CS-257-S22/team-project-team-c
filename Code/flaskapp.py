from random import sample
from flask import Flask, render_template, request
from importlib_metadata import NullFinder
import csv
import sys
from what2Eat import *

app = Flask(__name__)
database = ProductData("SmallProductSheet.csv")
data = []
helpMessage = "You can find all the ingredients of a product by going to http://127.0.0.1:5000/get_product_ingredients/[brandName]/[productName]. \
            \n Here is an example: \
            \n http://127.0.0.1:5000/get_product_ingredients/DCI Cheese Company, Inc./GREAT MIDWEST, CRANBERRY CHEDDAR \
            \n \
            \n You can also find all products carried by a certain brand by going to http://127.0.0.1:5000/get_all_products/[brandName] \
            \n Here is an example: \
            \n http://127.0.0.1:5000/get_all_products/Target Stores \
            \n You can check if a product contains something by going to http://127.0.0.1:5000/contains_ingredient/[ingredient]/[brandName]/[productName]\
            \n Here is an example: \
            \n http://127.0.0.1:5000/contains_ingredient/chickpeas/Target Stores/TRADITIONAL HUMMUS"

@app.route('/')
def homepage():
    """ Generate a homepage
    @return a homepage with instructions
    """ 
    return render_template('homepage.html', productList=database.get_product_list(), brandList=database.return_brands())
    #http://127.0.0.1:5000/

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/help')
def help():
    return render_template('help.html')
    
@app.route('/displayproducts')
def display_products():
    """ Generate a page that displays ingredients
    @return a page with a list of all products carried by the brand
    """ 
    brand = (request.args['brandSearch'])
    return render_template('products.html', brand=brand, products=database.get_all_products(brand))

@app.route('/displayingredients', methods=['POST'])
def display_ingredients():
    """ Generate a page that returns ingredients
    @return a page with a list of all ingredients of the product
    """ 
    product = (request.form['product'])
    rawIngredientsData = database.get_product_ingredients_product_only(product)
    intredientList = rawIngredientsData.split(",")
    # intredientList = ProductData.remove_comma(rawIngredientsData)
    return render_template('ingredients.html', product=product, ingredients=intredientList)

@app.errorhandler(404)
def page_not_found(e):
    """ Generate a page that returns ingredients
    @param 
        e: 404 error
    @return an error statement
    """ 
    return f'404 Page Not Found. {helpMessage}'

@app.errorhandler(500)
def python_bug(e):
    """ Generate a page that returns ingredients
    @param 
        e: 500 error
    @return an error statement
    """ 
    return f'500 Page Unavaiable. {helpMessage}'

if __name__ == '__main__':
    app.run()