from flaskapp import *
import unittest
import what2Eat 

class TestTwoMainFunction(unittest.TestCase):
    #unit test/integration test
    #if you wanna check if one method works no matter how the helper methods work, you need to create fake data
    def setUp(self):
        self.app = app.test_client()
        
    def test_get_ingredients(self):
        '''Retreiving the ingreident list from 
        valid inputs for product and brand name.'''
        response = self.app.get('/getProductIngredients/Target Stores/TRADITIONAL HUMMUS', follow_redirects=True)
        self.assertEqual(b'TRADITIONAL HUMMUS from Target Stores contains: chickpeas, water, sesame tahini, canola/olive oil blend, salt, citric acid, natural flavor, garlic, spices, potassium sorbate and sodium benzoate (to maintain freshness).', response.data)
    
    def test_invalid_product_get_ingredients(self):
        '''Edge case: user inputs invalid product name'''
        response = self.app.get('/getProductIngredients/Target Stores/HUMMUS', follow_redirects=True)
        self.assertEqual(b'HUMMUS from Target Stores contains: None', response.data)
    
    def test_invalid_brand_get_ingredients(self):
        '''Edge case: user inputs invalid brand name'''
        response = self.app.get('/getProductIngredients/Target/TRADITIONAL HUMMUS', follow_redirects=True)
        self.assertEqual(b'TRADITIONAL HUMMUS from Target contains: None', response.data)
    
    def test_contains_ingredient(self):
        '''Checking if a product contains ingreident'''
        response = self.app.get('/containsIngredient/chickpeas/Target Stores/TRADITIONAL HUMMUS', follow_redirects=True)
        print(response.data)
        self.assertEqual(b'TRADITIONAL HUMMUS from Target Stores contains chickpeas', response.data)

if __name__ == '__main__':
    unittest.main()
