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

    for row in productData:
        brand = row[1]
        if brand not in allBrands and brand: 
            allBrands.append(brand)

    allBrands.remove('brand_name') #remove the column name   
    return allBrands 


'''
Helper method to check if user input is a valid brand. Iterates through allbrand list to check. 
Input: brand name taken from user 
Outpu: boolean. True if brand exists. False if it does not. 
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

        for row in productData: 
            if row[1] == brandName:
                productName = row[0].lower() #convert product name into lowercase characters 
                productList.append(productName)

        return productList


'''
Input: brand and product
Returns: the list of ingredients 
'''
def getProductIngredients(brandName, productName):
    productData = load_csv_file("SmallProductSheet.csv") #product data continaing name, brand, and ingredients 
    
    for row in productData:
        if row[0] == productName and row[1] == brandName:
            return row[2].lower() #convert to lower case 
            # might be useful to return a list instead of a string
    
    
'''
Input: brand, product, and ingredient (string)
Returns: True if the product contains the ingredient, False otherwise 
'''
def containsIngredient(ingredient, brandName, productName):
    if not isValidBrand(brandName): 
        return False
    
    if not brandCarriesProduct(brandName, productName):
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
    if not isValidBrand(brandName): 
        return False

    allBrandProducts = getAllProducts(brandName)

    if productName in allBrandProducts:
        return True
    else:
        return False 
            
if __name__ == "__main__":

    if sys.argv[1] == 'getProductIngredients':
        brandName = sys.argv[2]
        productName = sys.argv[3].upper()
        print(getProductIngredients(brandName, productName))
    
    elif sys.argv[1] == 'getAllProducts':
        brandName = sys.argv[2]
        print(getAllProducts(brandName))

    else:
        print("Incorrect argument(s)")

    #TESTING STUFF - uncomment the line(s) you want to test. 
    #print(returnBrands())
    #print(getAllProducts("FRESH & EASY"))
    #print(getProductIngredients('FRESH & EASY', 'BARBECUE SAUCE'))
    #print(containsIngredient('molasses', 'FRESH & EASY', 'BARBECUE SAUCE'))
    #print(brandCarriesProduct('FRESH & EASY', 'BARBECUE SAUCE'))


