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
        brands = what2Eat.returnBrands("./emptyFileForTesting.csv")

    def test_returnBrandsFileNotFound(self):
        with self.assertRaises(FileNotFoundError):
            brands = what2Eat.returnBrands('')
    


if __name__ == '__main__':
    unittest.main()