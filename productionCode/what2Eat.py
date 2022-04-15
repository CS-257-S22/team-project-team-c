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
Helper method to check if user input is a valid brand 
'''
def isValidBrand(brandName):
    allBrands = returnBrands()
    if brandName in allBrands:
        return True
    else: 
        print("The brand is non-existent or mispelled. The list of brands are: ") #Error message 
        print(allBrands)
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
            return item[2].lower() #convert to lower case 
    
    
'''
Input: brand, product, and ingredient (string)
Returns: True if the product contains the ingredient, False otherwise 
'''
def containsIngredient(ingredient, brandName, productName):
    if not isValidBrand(brandName): 
        return False

    ingredients = getProductIngredients(brandName, productName)

    if ingredient in ingredients:
        return True
    else:
        return False

'''
Input: brand, product (string)
Returns: True if the brand sells the product, False otherwise. 
'''
def brandCarriesProduct(brandName, productName): 
    allBrandProducts = getAllProducts(brandName)

    if productName in allBrandProducts:
        return True
    else:
        return False 
            
    

def main():
    #TESTING STUFF - uncomment the line(s) you want to test. 
    #print(getAllProducts("FRESH & EASY"))
    #print(getProductIngredients('FRESH & EASY', 'BARBECUE SAUCE'))
    print(containsIngredient('molasses', 'RESH & EASY', 'BARBECUE SAUCE'))
    #print(brandCarriesProduct('FRESH & EASY', 'BARBECUE SAUCE'))
main()
