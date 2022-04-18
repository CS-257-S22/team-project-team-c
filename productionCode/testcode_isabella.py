import unittest
from what2Eat import *


'''Testing fucntions pertaining to the'ingredient' feature.'''

class TestIngredients(unittest.TestCase):
    'TESTING BASIC FUNCTIONALITY'
    def test_getIngredients(self):
        testData = what2Eat("SmallProductSheet.csv")
        ingredients = testData.getProductIngredients("Target Stores", "ROASTED RED PEPPER HUMMUS")
        testIngredients = "CHICKPEAS, ROASTED RED PEPPERS, SESAME TAHINI, CANOLA/OLIVE OIL BLEND, SALT, CITRIC ACID, NATURAL FLAVOR, GARLIC, SPICES, ACACIA GUM, XANTHAN GUM, GUAR GUM, POTASSIUM SORBATE AND SODIUM BENZOATE (TO MAINTAIN FRESHNESS).".lower()
        self.assertEqual(ingredients, testIngredients)

    def test_containsIngredient(self):
        testData = what2Eat("SmallProductSheet.csv")
        testContainsIngredient = testData.containsIngredient("roasted red peppers", "Target Stores", "ROASTED RED PEPPER HUMMUS")
        self.assertEqual(testContainsIngredient, True)
    
    
    'TESTING EDGE CASES'
    def test_valid_column_names_csv(self):
        runFile = what2Eat("SmallProductSheet.csv")
        testData = runFile.load_csv_file()
        firstLine = testData[0]
        self.assertEqual(["product_name","brand_name","ingredients"], firstLine)
    
    def test_csv_correct_format(self): 
        runFile = what2Eat("SmallProductSheet.csv")
        testData = runFile.load_csv_file()
        testLine = testData[2]
        self.assertEqual(testLine, ["CHIPOTLE BARBECUE SAUCE", "FRESH & EASY","WATER, SUGAR, TOMATO PASTE, MOLASSES, DISTILLED VINEGAR, CONTAINS 2% OR LESS OF: CORN STARCH, SALT, DRIED CHIPOTLE PEPPER, NATURAL SMOKE FLAVOR, MUSTARD FLOUR, DRIED GARLIC, DRIED ONION, SPICES."])
        

    def test_getIngredients_from_empty_file(self):
        testData = what2Eat("emptyFileForTesting.csv")
        ingredients = testData.getProductIngredients("brand", "product")
        self.assertEqual(ingredients, None)

    def test_getIngredients_invalid_brand(self):
        testData = what2Eat("SmallProductSheet.csv")
        ingredients = testData.getProductIngredients("family fare", "barbecue sauce")
        self.assertEqual(ingredients, None)
    


    
    # def test_containsIngredient






    
if __name__ == '__main__':
    unittest.main()
