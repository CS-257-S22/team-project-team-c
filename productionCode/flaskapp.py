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
    return "hello, this is the homepage"
    #http://127.0.0.1:5000/
    
@app.route('/containsIngredients/<ingredient>/<brandName>/<productName>', strict_slashes=False)
def check_one_ingredient(ingredient, brandName, productName):
    if sampleData.containsIngredient(ingredient, brandName, productName): 
        return f'{productName} from {brandName} contains {ingredient}'
        
@app.route('/getProductIngredients/<brandName>/<productName>', strict_slashes=False)
def display_ingredients(brandName, productName):
    return f'{productName} from {brandName} contains: {sampleData.getProductIngredients(brandName, productName)}'
    #http://127.0.0.1:5000/getProductIngredients/FRESH%20&%20EASY/BARBECUE%20SAUCE

@app.route('/containsIngredients/<ingredient>/<brandName>/<productName>', strict_slashes=False)
def check_one_ingredient(ingredient, brandName, productName):
    if sampleData.containsIngredient(ingredient, brandName, productName): 
        return f'{productName} from {brandName} contains {ingredient}'

@app.errorhandler(404)
def page_not_found(e):
    return "sorry, wrong format..."

@app.errorhandler(500)
def python_bug(e):
    return "Eek, a bug!"

if __name__ == '__main__':
    app.run()