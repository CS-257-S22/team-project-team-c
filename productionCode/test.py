import unittest
from webbrowser import get
from what2Eat import *


class TestWhat2Eat(unittest.TestCase):
    def setUp(self):
        """Set the files used to test functions
        Written by Kana"""
        self.defaultSampleData = what2Eat("SmallProductSheet.csv")
        self.EmptySampleData = what2Eat("emptyFileForTesting.csv")
        self.tenSampleData = what2Eat("10LinesForTesting.csv")

    def test_getIngredients(self):
        """Testing if the function getProductIngredients returns correct ingredients 
        Written by Isabella"""
        ingredients = self.defaultSampleData.getProductIngredients("Target Stores", "ROASTED RED PEPPER HUMMUS")
        testIngredients = "CHICKPEAS, ROASTED RED PEPPERS, SESAME TAHINI, CANOLA/OLIVE OIL BLEND, SALT, CITRIC ACID, NATURAL FLAVOR, GARLIC, SPICES, ACACIA GUM, XANTHAN GUM, GUAR GUM, POTASSIUM SORBATE AND SODIUM BENZOATE (TO MAINTAIN FRESHNESS).".lower()
        self.assertEqual(ingredients, testIngredients)

    def test_containsIngredient(self):
        """Testing if the function containsIngredient returns True when getting appropriate inputs 
        Written by Isabella"""
        result = self.defaultSampleData.containsIngredient("chickpeas", "Target Stores", "ROASTED RED PEPPER HUMMUS")
        self.assertTrue(result)

    def test_getIngredients_from_empty_file(self):
        """Testing if the function getProductIngredients returns None when attempting to retreive ingredients from an empty file 
        Written by Isabella"""
        ingredients = self.EmptySampleData.getProductIngredients("brand", "product")
        self.assertEqual(ingredients, None)
    
    def test_getIngredients_invalid_brand(self):
        """Testing if the function getProductIngredients returns None when getting an invalid brand name
        Written by Isabella"""
        ingredients = self.defaultSampleData.getProductIngredients("family fare", "barbecue sauce")
        self.assertEqual(ingredients, None)

if __name__ == '__main__':
    unittest.main()
        
        
    # def test_load_csv_file(self):
    #     """Testing the function loadCSVFile 
    #     Written by Alice"""
    #     testFile = what2Eat("SmallProductSheet.csv")
    #     productData = testFile.load_csv_file()
    #     firstRow = productData[1]
    #     testData = ["MOCHI ICE CREAM BONBONS","G. T. Japan, Inc.","ICE CREAM INGREDIENTS: MILK, CREAM, SUGAR, STRAWBERRIES (STRAWBERRIES, SUGAR), CORN SYRUP SOLIDS, SKIM MILK, WHEY, NATURAL FLAVOR, GUAR GUM, MONO & DIGLYCERIDES, BEET JUICE AND BEET POWDER (FOR COLOR), CELLULOSE GUM, LOCUST BEAN GUM, CARRAGEENAN. COATING INGREDIENTS: SUGAR, WATER, RICE FLOUR, TREHALOSE, EGG WHITES, BEET JUICE AND BEET POWDER (FOR COLOR), DUSTED WITH CORN & POTATO STARCH"]
    #     self.assertEqual(testData, firstRow)

# class TestHasIngredients(unittest.TestCase):
#     def test_has_ingredient(self):
#         """Testing the function hasIngredients
#         written by Isabella """
#         result = hasIngredient("garlic".upper(), "Roasted Garlic Hummus", "Target")
#         self.assertEqual(result, True)
        
#        """The following Tests were written by Alice """"
# class TestLoadCSVFile(unittest.TestCase):
#     def test_load_csv_file(self):
#         """Testing the function loadCSVFile written by Alice"""
#         productData = load_csv_file("SmallProductSheet.csv")
#         testData = [["MOCHI ICE CREAM BONBONS"],["G. T. Japan", "Inc."],["MILK, CREAM, SUGAR"]]
       
#         self.assertEqual(productData, testData)

# class TestValidBrandName(unittest.TestCase):
#     def test_is_Valid_Brand_True(self):
#         """Testing the function is_Valid_Brand written by Alice. This test takes in real brand and isValidBrand is expected to
#         return true. """
       
#         validBrandBool = isValidBrand("G. T. Japan, Inc")
#         self.assertEqual(validBrandBool, True)

#     def test_is_Valid_Brand_False(self):
#         """Testing the function is_Valid_Brand written by Alice. This test makes
#          sure that method returns false when the brand is invalid"""
#         invalidBrandBool = validBrand("G. T. China, Inc")
#         self.assertEqual(invalidBrandBool, False)

        
