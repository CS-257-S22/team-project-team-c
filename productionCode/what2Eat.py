import string
import sys 
import csv 
"""def getBrandName ():
    argList = sys.argv

    if (len(argList) == 2 ):
        print("you have entered correct brand nums!")
        brandName = argList[1]
        return brandName  
    else: 
       print("you have entered the wrong arguments bestie")
       return  

brandName = getBrandName()"""

'''
Load information from a .csv file
Input: file name (should be .csv format)
Output: a nested 2D list of product data 
'''
def load_csv_file(filename):
    productData = [] #contains product name, brand, and ingredients 
    with open(filename, 'r') as data:
        for line in csv.reader(data):
            productData.append(line)

    return productData




def getAllProducts(brandName):
    # get a brand name from the user (calls getUserBrandInput)
    productData = load_csv_file("SmallProductSheet.csv")
    productList = []
    for line in productData: 
        if line[1] == brandName:
            productList.append(line[0])
    return productList
    
print(getAllProducts("FRESH & EASY"))

# def getProductIngredients(brandName, productName):
   #load csv file
   # isolate by brand
   # isolate by product
   # return ingredient list  
