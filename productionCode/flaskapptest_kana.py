"""
    File@ flaskapptest_kana.py
    Author@ Kana Hashimoto
"""
from random import sample
from flask import Flask
import csv
import sys
from what2Eat import *

app = Flask(__name__)
sampleData = what2Eat('SmallProductSheet.csv')
data = []
@app.route('/') #http://127.0.0.1:5000/
def homepage():
    """ Generate a homepage
    @return a homepage with instructions
    """ 
    return "You can find all the ingredients of a product by going to http://127.0.0.1:5000/getProductIngredients/[brandName]/[productName]. \
            \n Here is an example: \
            \n http://127.0.0.1:5000/getProductIngredients/DCI Cheese Company, Inc./GREAT MIDWEST, CRANBERRY CHEDDAR \
            \n \
            \n You can also find all products carried by a certain brand by going to http://127.0.0.1:5000/getAllProducts/[brandName] \
            \n Here is an example: \
            \n http://127.0.0.1:5000/getAllProducts/Target Stores"

@app.route('/getProductIngredients/<brandName>/<productName>', strict_slashes=False)
def display_ingredients(brandName, productName):
    """ Generate a page that returns ingredients
    @param 
        brandName: a brand name that a user want to search with
        productName: a product name that a user want to search with
    @return a list of all ingredients of the product
    """ 
    return f'{productName} from {brandName} contains: {sampleData.getProductIngredients(brandName, productName)}'
    #examples:
    #http://127.0.0.1:5000/getProductIngredients/FRESH%20&%20EASY/BARBECUE%20SAUCE
    #http://127.0.0.1:5000/getProductIngredients/DCI%20Cheese%20Company,%20Inc./GREAT%20MIDWEST,%20CRANBERRY%20CHEDDAR

@app.route('/getAllProducts/<brandName>', strict_slashes=False)
def display_products(brandName):
    """ Generate a page that returns ingredients
    @param 
        brandName: a brand name that a user want to search with
    @return a list of all products carried by the brand
    """ 
    return f'{brandName} carries: {sampleData.getAllProducts(brandName)}'
    #examples:
    #return str(sampleData.getProductIngredients(brandName, productName))
    #http://127.0.0.1:5000/getAllProducts/FRESH%20&%20EASY
    
@app.errorhandler(404)
def page_not_found(e):
    """ Generate a page that returns ingredients
    @param 
        e: 404 error
    @return an error statement
    """ 
    return "Sorry, wrong format. Go to http://127.0.0.1:5000/ and check the correct format."

@app.errorhandler(500)
def python_bug(e):
    """ Generate a page that returns ingredients
    @param 
        e: 500 error
    @return an error statement
    """ 
    return "Eek, a bug!"

if __name__ == '__main__':
    app.run()