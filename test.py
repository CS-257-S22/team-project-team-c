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
