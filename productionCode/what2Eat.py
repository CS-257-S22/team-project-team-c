import string
import sys 
import csv 

'''Loads information from a .csv file. Each row is represented as a list within a larger list.
Input: file name (should be .csv format)
Return: a nested 2D list of product data 
'''
def load_csv_file(filename):
    productData = [] #contains product name, brand, and ingredients 
    with open(filename, 'r') as data:
        for line in csv.reader(data):
            productData.append(line)

    return productData

'''
Helper method to return all brands as a list
'''
def returnBrands():
    productData = load_csv_file("SmallProductSheet.csv")
    allBrands = []

    for item in productData:
        brand = item[1]
        if brand not in allBrands and brand: 
            allBrands.append(brand)

    allBrands.remove('brand_name') #remove the column name 

    return allBrands 

'''
Helper method to display (print) all brands as a list
'''
def displayBrands():
    productData = load_csv_file("SmallProductSheet.csv")
    allBrands = []

    for item in productData:
        brand = item[1]
        if brand not in allBrands and brand: 
            allBrands.append(brand)

    allBrands.remove('brand_name') #remove the column name 

    print(allBrands) 

'''
Helper method to check if user input is a valid brand 
'''
def isValidBrand(brandName):
    allBrands = returnBrands()
    if brandName in allBrands:
        return True
    else: 
        print("The brand is non-existent or mispelled. The list of brands are: ") #Error message 
        displayBrands()
        return False


'''
Input: brand name 
Returns: a list of all products carried by the given brand. 
'''
def getAllProducts(brandName):

    if isValidBrand(brandName):
        productData = load_csv_file("SmallProductSheet.csv") #product data continaing name, brand, and ingredients 
        productList = []

        for item in productData: 
            if item[1] == brandName:
                productList.append(item[0])

        return productList


'''
Input: brand and product
Returns: the list of ingredients 
'''
def getProductIngredients(brandName, productName):
    productData = load_csv_file("SmallProductSheet.csv") #product data continaing name, brand, and ingredients 
    
    for item in productData:
        if item[0] == productName and item[1] == brandName:
            print(item[2])
    
    



# def main():
#     #TESTING STUFF 
#     #print(getAllProducts("FRESH & EASY"))
# getProductIngredients('FRESH & EASY', 'BARBECUE SAUCE')


