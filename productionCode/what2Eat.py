import string
import sys 
import csv 


'''Loads information from a .csv file. Each row is represented as a list within a larger list.
Input: file name (should be .csv format)
Return: a nested 2D list of product data 
'''

class what2Eat:
    def __init__(self, fileName):
        self.fileName = fileName

    def load_csv_file(self):
        productData = [] #contains product name, brand, and ingredients 
        with open(self.fileName, 'r') as data:
            for line in csv.reader(data):
                productData.append(line)

        return productData

    '''
    Helper method to return all brands as a list
    '''
    def returnBrands(self):
        productData = self.load_csv_file()
        allBrands = []

        for row in productData:
            brand = row[1]
            if brand and brand not in allBrands: 
                allBrands.append(brand)

        allBrands.remove('brand_name') #remove the column name   
        return allBrands 


    '''
    Helper method to check if user input is a valid brand. Iterates through allbrand list to check. 
    Input: brand name taken from user 
    Outpu: boolean. True if brand exists. False if it does not. 
    '''
    def isValidBrand(self, brandName):
        allBrands = self.returnBrands()
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
    def getAllProducts(self, brandName):
        
        if self.isValidBrand(brandName):
            productData = self.load_csv_file() #product data continaing name, brand, and ingredients 
            productList = []

            for row in productData: 
                if row[1] == brandName:
                    productList.append(row[0])
                    

            return productList


    '''
    Input: brand and product
    Returns: the list of ingredients that the given product contains 
    '''
    def getProductIngredients(self, brandName, productName):
        productData = self.load_csv_file() #product data continaing name, brand, and ingredients 
        
        for row in productData:
            if row[0] == productName and row[1] == brandName:
                return row[2].lower() #convert to lower case 
        
        
    '''
    Input: brand, product, and ingredient (string)
    Returns: True if the product contains the ingredient, False otherwise 
    '''
    def containsIngredient(self, ingredient, brandName, productName):
        if not self.isValidBrand(brandName): 
            return False
        
        if not self.brandCarriesProduct(brandName, productName):
            return False

        ingredients = self.getProductIngredients(brandName, productName)

        if ingredient in ingredients:
            return True
        else:
            return False

    '''
    Input: brand, product (string)
    Returns: True if the brand sells the product, False otherwise. 
    '''
    def brandCarriesProduct(self, brandName, productName): 
        if not self.isValidBrand(brandName): 
            return False

        allBrandProducts = self.getAllProducts(brandName)

        if productName in allBrandProducts:
            return True
        else:
            return False 
                           
    def printHelpPage():

        helpStatement =  "Welcome to What2Eat!\nPlease refer to the following instructions to navigate our interface.\n In order to use the USDA food database we reccomend you use SmallProductSheet.csv for your file.\n To look up products by brand enter the following into the terminal:                   python what2Eat.py getAllProducts [brandname] [fileName]\n to look up the nutrients of a specific product enter the following into the terminal: python what2Eat.py getIngredients [brandname] [productName] [fileName]\n"
        return helpStatement
    # if __name__ == '__main__':    
        #TESTING STUFF - uncomment the line(s) you want to test. 
        #print(returnBrands())
        #print(getAllProducts("FRESH & EASY"))
        #print(getProductIngredients('FRESH & EASY', 'BARBECUE SAUCE'))
        #print(containsIngredient('molasses', 'FRESH & EASY', 'BARBECUE SAUCE'))

dataFromSmallProductSheet = what2Eat("SmallProductSheet.csv")

#print(dataFromSmallProductSheet.brandCarriesProduct('FRESH & EASY', 'BARBECUE SAUCE'))
if len(sys.argv) > 1:
    if sys.argv[1] == 'getProductIngredients':
        brandName = sys.argv[2]
        productName = sys.argv[3].upper()
        fileName = sys.argv[4]
        sampleData = what2Eat(fileName)
        print(sampleData.getProductIngredients(brandName, productName))

    elif sys.argv[1] == 'getAllProducts':
        brandName = sys.argv[2]
        fileName = sys.argv[3]
        sampleData = what2Eat(fileName)
        print(sampleData.getAllProducts(brandName))

    elif sys.argv[1] == 'help':
        text = printHelpPage()


    else:
        print("Incorrect argument(s)")

