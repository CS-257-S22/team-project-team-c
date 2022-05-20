from random import sample
import string
import os
import sys 
import csv 
import argparse
from pkg_resources import require

sys.path.append("/Users/kana/Desktop/team-project-team-c/Backend")
from datasource import *

class ProductData:
    def __init__(self, fileName):
        self.source = DataSource()
    
    def return_brands(self):
        """
        Helper method to return all brands as a list.
        Returns: 
            allBrands: a list of all brands
        """
        allBrands = []
        for row in self.productData:
            brand = row[1]
            if brand and brand not in allBrands: 
                allBrands.append(brand)

        # if 'brand_name' in allBrands:
        #     allBrands.remove('brand_name') #remove the column name    
        return allBrands 

    def is_valid_brand(self, brandName):
        """
        Helper method to check if user input is a valid brand. Iterates through allbrand list to check. 
        Args: 
            brandName (str): brand name taken from user 
        Returns: 
            a boolean value that is True if the brand exists and False if it does not. 
        """
        allBrands = self.return_brands()
        if brandName in allBrands:
            return True
        else: 
            print("The brand is non-existent or mispelled. The list of brands are: ") #Error message 
            print(allBrands)
            return False

    #New function for flaskapp written by Kana
    def get_product_list(self):
        productData = self.load_csv_file()
        productList = []
        for row in productData:
            productList.append(row[0])
        return productList

    def get_all_products(self, brandName):
        """
        Helper method to return all products carried by the given brand.
        Args:
            brandName (str): brand name taken from user 
        Returns:
            productList: a list of all products carried by the given brand
        """
        if self.is_valid_brand(brandName):
            productData = self.load_csv_file() #product data continaing name, brand, and ingredients 
            productList = []
            for row in productData: 
                if row[1] == brandName:
                    productList.append(row[0])
            return productList

    #New function for flaskapp written by Kana
    # def remove_comma(String):
    #     newList = list(String)
    #     for index in range(len(newList)):
    #         if newList[index] == '(': 
    #             for i in range(index, len(newList)):
    #                 if newList[i] == ',':
    #                     newList[i] = ' /'
    #                 elif newList[i] == ')':
    #                     break
    #         newData = "".join(newList)
    #         newData = newData.split(",")
    #     return newData

    #New function for flaskapp written by Kana
    def get_product_ingredients_by_product(self, productName):
        """
        Method to return ingredients of the given product carried by the brand.
        Args:
            productName (str): product name taken from user
        Returns:
            a string of all the ingredients
        """
        productData = self.load_csv_file() #product data continaing name, brand, and ingredients 
        for row in productData:
            if row[0] == productName:
                return row[2].lower() #convert to lower case 

    def get_product_ingredients(self, brandName, productName):
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
        
    def contains_ingredient(self, ingredient, brandName, productName):
        """
        Method to check if the given product carried by the brand contains the user input ingredient
        Args:
            ingredient (str): ingredient taken from user 
            brandName (str): brand name taken from user 
            productName (str): product name taken from user 
        Returns:
            a boolean value that is True if the product contains the ingredient and False if it does not. 
        """
        if not self.is_valid_brand(brandName): 
            return False
        
        elif not self.brand_carries_product(brandName, productName):
            return False

        else:
            ingredients = self.get_product_ingredients(brandName, productName)
            if ingredient in ingredients:
                return True
            else:
                return False

    def brand_carries_product(self, brandName, productName): 
        """
        Method to check if the given brand carries the product 
        Args:
            brandName (str): brand name taken from user 
            productName (str): product name taken from user 
        Returns:
            a boolean value that is True if the brand carries the product and False if it does not. 
        """
        if not self.is_valid_brand(brandName): 
            return False
        else:
            allBrandProducts = self.get_all_products(brandName)
            if productName in allBrandProducts:
                return True
            else:
                return False 
        
if __name__ == '__main__': 

    my_parser = argparse.ArgumentParser(description="Welcome to What2Eat!\n Please refer to the following instructions to navigate our interface.\n In order to use the USDA food database we recommend you use SmallProductSheet.csv for your file.\n To look up products by brand enter the following into the terminal:                   python what2Eat.py getAllProducts [brandname] [fileName]\n to look up the nutrients of a specific product enter the following into the terminal: python what2Eat.py getIngredients [brandname] [productName] [fileName]\n")
    my_parser.add_argument('functionName', help='the name of the function you want to use')
    my_parser.add_argument('-b','--brandName', help= 'the name of the brand you want to look up (should be a string)')
    my_parser.add_argument('-p','--productName', help= 'the name of product you want to look up (should be a string)')
    my_parser.add_argument('-f','--fileName', help= 'the file you want to search in (default is FinalData.csv)', default='FinalData.csv')
    args = my_parser.parse_args()
    sampleData = ProductData()

    if args.functionName == 'get_product_ingredients':
    print(sampleData.get_all_products('DCI Cheese Company, Inc.'))
        print(sampleData.get_product_ingredients(args.brandName, args.productName))
        my_source = DataSource()
        my_source.get_all_products('DCI Cheese Company, Inc.')
        my_source.get_all_ingredients('MOCHI ICE CREAM BONBONS')
        # command line example
        # python3 what2Eat.py get_product_ingredients -b 'FRESH & EASY' -p 'BARBECUE SAUCE'

    elif args.functionName == 'get_all_products':
        print(sampleData.get_all_products(args.brandName))
        # command line example
        # python3 what2Eat.py get_all_products -b 'FRESH & EASY' 

    else:
        print("Incorrect argument(s)")
