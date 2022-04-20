import unittest
from what2Eat import *


'''The following tests pertain to the 'getIngredient' feature and its helper functions.'''

#Global variables
sampleData1 = ProductData("SmallProductSheet.csv")
sampleData2 = ProductData("emptyFileForTesting.csv")
testData1 = sampleData1.load_csv_file()
testData2 = sampleData2.load_csv_file()



class TestIngredients(unittest.TestCase):
    'TESTING BASIC FUNCTIONALITY'
    def test_getIngredients(self):
        ingredients = sampleData1.getProductIngredients("Target Stores", "ROASTED RED PEPPER HUMMUS")
        testIngredients = "CHICKPEAS, ROASTED RED PEPPERS, SESAME TAHINI, CANOLA/OLIVE OIL BLEND, SALT, CITRIC ACID, NATURAL FLAVOR, GARLIC, SPICES, ACACIA GUM, XANTHAN GUM, GUAR GUM, POTASSIUM SORBATE AND SODIUM BENZOATE (TO MAINTAIN FRESHNESS).".lower()
        self.assertEqual(ingredients, testIngredients)


    def test_containsIngredient(self):
        result = sampleData1.containsIngredient("chickpeas", "Target Stores", "ROASTED RED PEPPER HUMMUS")
        self.assertTrue(result)
                    

    'TESTING EDGE CASES'
    def test_valid_column_names_csv(self):
        '''Checks that the  dataset contains the columns: 
        brand name, product name, and ingredients (in that order). 
        '''
        firstLine = testData1[0]
        self.assertEqual(["product_name","brand_name","ingredients"], firstLine)
    
    def test_csv_file_has_ingredients(self): 
        '''Checks that the third column of the dataset contains the ingredient information.'''
        testLine = testData1[2]
        self.assertEqual(testLine, ["CHIPOTLE BARBECUE SAUCE", "FRESH & EASY","WATER, SUGAR, TOMATO PASTE, MOLASSES, DISTILLED VINEGAR, CONTAINS 2% OR LESS OF: CORN STARCH, SALT, DRIED CHIPOTLE PEPPER, NATURAL SMOKE FLAVOR, MUSTARD FLOUR, DRIED GARLIC, DRIED ONION, SPICES."])
        

    def test_getIngredients_from_empty_file(self):
        '''Checks that attempting to retreive ingredients from an empty file should return None'''
        ingredients = sampleData2.getProductIngredients("brand", "product")
        self.assertEqual(ingredients, None)

    def test_getIngredients_invalid_brand(self):
        ingredients = sampleData1.getProductIngredients("family fare", "barbecue sauce")
        self.assertEqual(ingredients, None)
    

if __name__ == '__main__':
    unittest.main()
