class TestWhat2Eat(unittest.TestCase):
    def test_compareNutrients(self):
        """Sample test for compareNutrients"""
        nutrients = ["protein", "sugar", "vitaminC", "riboflavin", "transfat"]
        providedNutrients = ["protein", "sugar", "vitaminC"]

        self.assertEqual(nutrients, providedNutrients)
