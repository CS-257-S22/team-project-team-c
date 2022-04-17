import unittest
import what2eat

class TestWhat2Eat(unittest.TestCase):
    def test_compareNutrients(self):
        """Sample test for compareNutrients"""
        nutrients = ["protein", "sugar", "vitaminC", "riboflavin", "transfat"]
        providedNutrients = ["protein", "sugar", "vitaminC"]

        self.assertEqual(nutrients, providedNutrients)
        
class TestHasIngredients(unittest.TestCase):
    def test_has_ingredient(self):
        """Testing the function hasIngredients
        written by Isabella """
        result = hasIngredient("garlic".upper(), "Roasted Garlic Hummus", "Target")
        self.assertEqual(result, True)
        
       """The following Tests were written by Alice """"
class TestLoadCSVFile(unittest.TestCase):
    def test_load_csv_file(self):
        """Testing the function loadCSVFile written by Alice"""
        productData = load_csv_file("SmallProductSheet.csv")
        testData = [["MOCHI ICE CREAM BONBONS"],["G. T. Japan", "Inc."],["MILK, CREAM, SUGAR"]]
       
        self.assertEqual(productData, testData)

class TestValidBrandName(unittest.TestCase):
    def test_is_Valid_Brand_True(self):
        """Testing the function is_Valid_Brand written by Alice. This test takes in real brand and isValidBrand is expected to
        return true. """
       
        validBrandBool = isValidBrand("G. T. Japan, Inc")
        self.assertEqual(validBrandBool, True)

    def test_is_Valid_Brand_False(self):
        """Testing the function is_Valid_Brand written by Alice. This test makes
         sure that method returns false when the brand is invalid"""
        invalidBrandBool = validBrand("G. T. China, Inc")
        self.assertEqual(invalidBrandBool, False)

        
