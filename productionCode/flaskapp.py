from random import sample
from flask import Flask
import csv
import sys
from what2Eat import *

app = Flask(__name__)
sampleData = ProductData('SmallProductSheet.csv')
data = []
@app.route('/')

def homepage():
    """ Generate a homepage
    @return a homepage with instructions
    """ 
    return "You can find all the ingredients of a product by going to http://127.0.0.1:5000/get_product_ingredients/[brandName]/[productName]. \
            \n Here is an example: \
            \n http://127.0.0.1:5000/get_product_ingredients/DCI Cheese Company, Inc./GREAT MIDWEST, CRANBERRY CHEDDAR \
            \n \
            \n You can also find all products carried by a certain brand by going to http://127.0.0.1:5000/get_all_products/[brandName] \
            \n Here is an example: \
            \n http://127.0.0.1:5000/get_all_products/Target Stores \
            \n You can check if a product contains something by going to http://127.0.0.1:5000/contains_ingredient/[ingredient]/[brandName]/[productName]\
            \n Here is an example: \
            \n http://127.0.0.1:5000/contains_ingredient/chickpeas/Target Stores/TRADITIONAL HUMMUS"

    #http://127.0.0.1:5000/
    
@app.route('/get_all_products/<brandName>', strict_slashes=False)
def display_products(brandName):
    """ Generate a page that returns ingredients
    @param 
        brandName: a brand name that a user want to search with
    @return a list of all products carried by the brand
    """ 
    return f'{brandName} carries: {sampleData.get_all_products(brandName)}'
    #example:
    #http://127.0.0.1:5000/get_all_products/FRESH%20&%20EASY

@app.route('/get_product_ingredients/<brandName>/<productName>', strict_slashes=False)
def display_ingredients(brandName, productName):
    """ Generate a page that returns ingredients
    @param 
        brandName: a brand name that a user want to search with
        productName: a product name that a user want to search with
    @return a list of all ingredients of the product
    """ 
    return f'{productName} from {brandName} contains: {sampleData.get_product_ingredients(brandName, productName)}'
    #examples:
    #http://127.0.0.1:5000/get_product_ingredients/FRESH%20&%20EASY/BARBECUE%20SAUCE


@app.route('/contains_ingredient/<ingredient>/<brandName>/<productName>', strict_slashes=False)
def display_contains_ingredient(ingredient, brandName, productName):
    """ Generate a page that tells if a production contains a certain ingredient
    @param 
        ingredient: the ingredient 
        brandName: a brand name that a user want to search with
        productName: a product name that a user want to search with
    @return verifies that the product contains the ingredient.
    For negative instances (invalid brand, invalid product, does not contain ingredient), returns None.  
    """ 
    if sampleData.contains_ingredient(ingredient, brandName, productName): 
        return f'{productName} from {brandName} contains {ingredient}'
    else: 
        return f'{productName} from {brandName} does not contain {ingredient} or invalid input' 
    #true: http://127.0.0.1:5000/contains_ingredient/chickpeas/Target Stores/TRADITIONAL HUMMUS
    #false: http://127.0.0.1:5000/contains_ingredient/fake peas/Target Stores/TRADITIONAL HUMMUS

@app.errorhandler(404)
def page_not_found(e):
    """ Generate a page that returns ingredients
    @param 
        e: 404 error
    @return an error statement
    """ 
    return "404 Page Not Found. Go to http://127.0.0.1:5000/ and check the correct format."

@app.errorhandler(500)
def python_bug(e):
    """ Generate a page that returns ingredients
    @param 
        e: 500 error
    @return an error statement
    """ 
    return "500 Page Unavaiable. Go to http://127.0.0.1:5000/ and check the correct format."

if __name__ == '__main__':
    app.run()