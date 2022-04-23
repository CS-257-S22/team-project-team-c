from flaskapp import *
import unittest
import what2Eat 

class TestTwoMainFunction(unittest.TestCase):
    #unit test/integration test
    #if you wanna check if one method works no matter how the helper methods work, you need to create fake data
    def setUp(self):
        """Set an app to test functions
        Written by Kana"""
        self.app = app.test_client()
    
    def test_homepage(self):
        """Test if the homepage displays the correct messages
        Written by Kana"""
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(b'You can find all the ingredients of a product by going to http://127.0.0.1:5000/get_product_ingredients/[brandName]/[productName]. \
            \n Here is an example: \
            \n http://127.0.0.1:5000/get_product_ingredients/DCI Cheese Company, Inc./GREAT MIDWEST, CRANBERRY CHEDDAR \
            \n \
            \n You can also find all products carried by a certain brand by going to http://127.0.0.1:5000/get_all_products/[brandName] \
            \n Here is an example: \
            \n http://127.0.0.1:5000/get_all_products/Target Stores \
            \n You can check if a product contains something by going to http://127.0.0.1:5000/contains_ingredient/[ingredient]/[brandName]/[productName]\
            \n Here is an example: \
            \n http://127.0.0.1:5000/contains_ingredient/chickpeas/Target Stores/TRADITIONAL HUMMUS', response.data)

    def test_display_products_success(self):
        """Test if the page displays all products
        Written by Kana"""
        response = self.app.get('/get_all_products/G. T. Japan, Inc.',follow_redirects=True)
        self.assertEqual(b"G. T. Japan, Inc. carries: ['MOCHI ICE CREAM BONBONS']", response.data)

    def test_display_products_fail(self):
        """Test if the page displays None when receiving a wrong brand name
        Written by Kana"""
        response = self.app.get('/get_all_products/random brand', follow_redirects=True)
        self.assertEqual(b'random brand carries: None', response.data)

    def test_get_ingredients(self):
        '''
        @Written by: Isabella
        Retreiving the ingreident list from 
        valid inputs for product and brand name.'''
        response = self.app.get('/get_product_ingredients/Target Stores/TRADITIONAL HUMMUS', follow_redirects=True)
        self.assertEqual(b'TRADITIONAL HUMMUS from Target Stores contains: chickpeas, water, sesame tahini, canola/olive oil blend, salt, citric acid, natural flavor, garlic, spices, potassium sorbate and sodium benzoate (to maintain freshness).', response.data)
    
    def test_invalid_product_get_ingredients(self):
        '''
        @Written by: Isabella
        Edge case: user inputs invalid product name'''
        response = self.app.get('/get_product_ingredients/Target Stores/HUMMUS', follow_redirects=True)
        self.assertEqual(b'HUMMUS from Target Stores contains: None', response.data)
    
    def test_display_ingredients_falseProduct_num(self):
        """Test if the page displays None when receiving a wrong product name (as a number)
        Edge case: user inputs invalid product name as a number
        Written by Kana"""
        response = self.app.get('/get_product_ingredients/FRESH & EASY/1031', follow_redirects=True)
        self.assertEqual(b'1031 from FRESH & EASY contains: None', response.data)

    def test_invalid_brand_get_ingredients(self):
        '''
        @Written by: Isabella
        Edge case: user inputs invalid brand name'''
        response = self.app.get('/get_product_ingredients/Target/TRADITIONAL HUMMUS', follow_redirects=True)
        self.assertEqual(b'TRADITIONAL HUMMUS from Target contains: None', response.data)
    
    def test_display_ingredients_falseBrand_num(self):
        """Test if the page displays None when receiving a wrong product name (as a number)
        Edge case: user inputs invalid brand name as a number
        Written by Kana"""
        response = self.app.get('/get_product_ingredients/1031/DICED TOMATOES', follow_redirects=True)
        self.assertEqual(b'DICED TOMATOES from 1031 contains: None', response.data)

    def test_display_ingredients_falseCombo(self):
        """Test if the page displays ingredients when receiving a wrong combination of an existing brand name and an existing product name
        Written by Kana"""
        response = self.app.get('/get_product_ingredients/Target Stores/DICED TOMATOES', follow_redirects=True)
        self.assertEqual(b'DICED TOMATOES from Target Stores contains: None', response.data)
    
    def test_contains_ingredient(self):
        '''
        @Written by: Isabella
        Checking if a product contains ingreident'''
        response = self.app.get('/contains_ingredient/chickpeas/Target Stores/TRADITIONAL HUMMUS', follow_redirects=True)
        print(response.data)
        self.assertEqual(b'TRADITIONAL HUMMUS from Target Stores contains chickpeas', response.data)


if __name__ == '__main__':
    unittest.main()
