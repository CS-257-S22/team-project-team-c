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


class TestHelpPage(unittest.TestCase):
    def test_is_Valid_Help_Page(self):
        """Testing to see if the help page information retunrs the correct information"""  
        testFile = what2Eat("SmallProductSheet.csv")
        returnedHelpPage= testFile.printHelpPage()
        testData = "Welcome to What2Eat!\nPlease refer to the following instructions to navigate our interface.\n In order to use the USDA food database we reccomend you use SmallProductSheet.csv for your file.\n To look up products by brand enter the following into the terminal:                   python what2Eat.py getAllProducts [brandname] [fileName]\n to look up the nutrients of a specific product enter the following into the terminal: python what2Eat.py getIngredients [brandname] [productName] [fileName]\n"
        self.assertEqual(testData, returnedHelpPage)


if __name__ == '__main__':
    unittest.main()