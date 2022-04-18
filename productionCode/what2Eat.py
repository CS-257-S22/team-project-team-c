import string
import os
import sys 
import csv 
import argparse
from pkg_resources import require

class what2Eat:
    def __init__(self, fileName):
        """
        what2Eat Class Constructor to initialize the object.
        Args: 
            fileName (str): the name of the file (should be .csv format)
        """
        self.fileName = fileName
    
    def load_csv_file(self):
        """
        Loads information from a .csv file. Each row is represented as a list within a larger list.
        Returns: 
            productData: a nested 2D list of product data 
        """
        productData = [] #contains product name, brand, and ingredients 
        with open(self.fileName, 'r') as data:
            for line in csv.reader(data):
                productData.append(line)
        return productData

    def returnBrands(self):
        """
        Helper method to return all brands as a list.
        Returns: 
            allBrands: a list of all brands
        """
        productData = self.load_csv_file()
        allBrands = []
        for row in productData:
            brand = row[1]
            if brand and brand not in allBrands: 
                allBrands.append(brand)
        allBrands.remove('brand_name') #remove the column name   
        return allBrands 

    def isValidBrand(self, brandName):
        """
        Helper method to check if user input is a valid brand. Iterates through allbrand list to check. 
        Args: 
            brandName (str): brand name taken from user 
        Returns: 
            a boolean value that is True if the brand exists and False if it does not. 
        """
        allBrands = self.returnBrands()
        if brandName in allBrands:
            return True
        else: 
            print("The brand is non-existent or mispelled. The list of brands are: ") #Error message 
            print(allBrands)
            return False

    def getAllProducts(self, brandName):
        """
        Helper method to return all products carried by the given brand.
        Args:
            brandName (str): brand name taken from user 
        Returns:
            productList: a list of all products carried by the given brand
        """
        productData = self.load_csv_file() #product data continaing name, brand, and ingredients 
        productList = []
        for row in productData: 
            if row[1] == brandName:
                productList.append(row[0])
        return productList

    def getProductIngredients(self, brandName, productName):
        """
        Method to return ingredients of the given product carried by the brand.
        Args:
            brandName (str): brand name taken from user 
            productName (str): product name taken from user
        Returns:
            a string of all the ingredients
        """
        productData = self.load_csv_file() #product data continaing name, brand, and ingredients 
        for row in productData:
            if row[0] == productName and row[1] == brandName:
                return row[2].lower() #convert to lower case 
        
    def containsIngredient(self, ingredient, brandName, productName):
        """
        Method to check if the given product carried by the brand contains the user input ingredient
        Args:
            ingredient (str): ingredient taken from user 
            brandName (str): brand name taken from user 
            productName (str): product name taken from user 
        Returns:
            a boolean value that is True if the product contains the ingredient and False if it does not. 
        """
        ingredients = self.getProductIngredients(brandName, productName)
        if ingredient in ingredients:
            return True
        else:
            return False

    def brandCarriesProduct(self, brandName, productName): 
        """
        Method to check if the given brand carries the product 
        Args:
            brandName (str): brand name taken from user 
            productName (str): product name taken from user 
        Returns:
            a boolean value that is True if the brand carries the product and False if it does not. 
        """
        allBrandProducts = self.getAllProducts(brandName)
        if productName in allBrandProducts:
            return True
        else:
            return False 
        
if __name__ == '__main__': 

    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('functionName', help='functionName')
    my_parser.add_argument('-b','--brandName', help= 'brandName')
    my_parser.add_argument('-p','--productName', help= 'productName')
    my_parser.add_argument('-f','--fileName', help= 'fileName', default='SmallProductSheet.csv')
    args = my_parser.parse_args()
    sampleData = what2Eat(args.fileName)

    if args.functionName == 'getProductIngredients':
        print(sampleData.getProductIngredients(args.brandName, args.productName))
        # command line example
        # python3 what2Eat.py getProductIngredients -b 'FRESH & EASY' -p 'BARBECUE SAUCE'

    elif args.functionName == 'getAllProducts':
        print(sampleData.getAllProducts(args.brandName))
        # command line example
        # python3 what2Eat.py getAllProducts -b 'FRESH & EASY' 

    else:
        print("Incorrect argument(s)")