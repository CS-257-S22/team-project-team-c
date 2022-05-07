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
    # for index in range(len(rawIngredientsData)):
    #     if rawIngredientsData[index] == '(': 
    #         for chInside in rawIngredientsData[index:]:
    #             if chInside == ',':
    #                 chInside = '/'
    #             elif chInside == ')':
    #                 break
    ingredientList = rawIngredientsData.split(',')
    return render_template('ingredients.html', product=product, ingredients=ingredientList)


# @app.route('/contains_ingredient/<ingredient>/<brandName>/<productName>', strict_slashes=False)
# def display_contains_ingredient(ingredient, brandName, productName):
#     """ Generate a page that tells if a production contains a certain ingredient
#     @param 
#         ingredient: the ingredient 
#         brandName: a brand name that a user want to search with
#         productName: a product name that a user want to search with
#     @return verifies that the product contains the ingredient.
#     For negative instances (invalid brand, invalid product, does not contain ingredient), returns None.  
#     """ 
#     if sampleData.contains_ingredient(ingredient, brandName, productName): 
#         return f'{productName} from {brandName} contains {ingredient}'
#     else: 
#         return f'{productName} from {brandName} does not contain {ingredient} or invalid input' 
#     #true: http://127.0.0.1:5000/contains_ingredient/chickpeas/Target Stores/TRADITIONAL HUMMUS
#     #false: http://127.0.0.1:5000/contains_ingredient/fake peas/Target Stores/TRADITIONAL HUMMUS

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