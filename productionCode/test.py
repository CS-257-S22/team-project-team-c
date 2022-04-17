import unittest
import what2Eat


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


class TestGetAllProducts(unittest.TestCase):
    # def _write_temp_csv_file(self):  # helper method
    #     pass

    def test_returnBrands(self):
        """Testing the helper function returnBrands. The test function uses a small""" 
        """sample of the dataset to compare results"""
        """Written by Morgan"""

        brands = what2Eat.returnBrands("dataForTesting.csv")
        accurateListOfBrands = ["G. T. Japan, Inc.","FRESH & EASY"]
        self.assertEqual(brands, accurateListOfBrands)

    def test_returnBrandsWithEmptyFile(self):
        """Testing the returnBrands handling of an empty file"""
        """Written by Morgan"""
        brands = what2Eat.returnBrands("productionCode/testData/emptyFileForTesting.csv")
        self.assertEqual([], brands)

    def test_returnBrandsFileNotFound(self):
        with self.assertRaises(FileNotFoundError):
            brands = what2Eat.returnBrands('')
   
    '''
    ideas:
        returnBrands should return brands (not ingredients, etc.)
        returnBrands should not return any "empty" brands if they exist in the CSV file.
        returnBrands should not return the same brand more than once (even if it appears twice in teh CSV file.)
        returnBrands returns brands in the order that they are found
        returnBrands does not include column label 
    '''


if __name__ == '__main__':
    unittest.main()