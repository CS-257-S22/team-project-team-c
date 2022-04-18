import unittest 
from webbrowser import get 
from what2Eat import *


class TestLoadCSVFile(unittest.TestCase):
    def test_load_csv_file(self):
        """Testing the function loadCSVFile written by Alice"""
        testFile = what2Eat("SmallProductSheet.csv")
        productData = testFile.load_csv_file()
        firstRow = productData[1]
        testData = ["MOCHI ICE CREAM BONBONS","G. T. Japan, Inc.","ICE CREAM INGREDIENTS: MILK, CREAM, SUGAR, STRAWBERRIES (STRAWBERRIES, SUGAR), CORN SYRUP SOLIDS, SKIM MILK, WHEY, NATURAL FLAVOR, GUAR GUM, MONO & DIGLYCERIDES, BEET JUICE AND BEET POWDER (FOR COLOR), CELLULOSE GUM, LOCUST BEAN GUM, CARRAGEENAN. COATING INGREDIENTS: SUGAR, WATER, RICE FLOUR, TREHALOSE, EGG WHITES, BEET JUICE AND BEET POWDER (FOR COLOR), DUSTED WITH CORN & POTATO STARCH"]

        
        self.assertEqual(testData, firstRow)
        

class TestValidBrandName(unittest.TestCase):
    def test_is_Valid_Brand_True(self):
        """Testing the function is_Valid_Brand written by Alice. This test takes in real brand and isValidBrand is expected to
        return true. """
        testFile = what2Eat("SmallProductSheet.csv")
        validBrandBool = testFile.isValidBrand("G. T. Japan, Inc.")
        self.assertEqual(validBrandBool, True)

    def test_is_Valid_Brand_False(self):
        """Testing the function is_Valid_Brand written by Alice. This test makes
         sure that method returns false when the brand is invalid"""
        testFile = what2Eat("SmallProductSheet.csv")

        invalidBrandBool =  testFile.isValidBrand("G. T. China, Inc.")
        
        self.assertEqual(invalidBrandBool, False)
      
if __name__ == '__main__':
    unittest.main()