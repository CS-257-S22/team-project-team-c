from flaskapp import *
import unittest
import what2Eat 

class TestTwoMainFunction(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_route(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(b'hello, this is the homepage', response.data)

    def test_display_products_success(self):
        response = self.app.get('/getAllProducts/G. T. Japan, Inc.',follow_redirects=True)
        self.assertEqual(b"G. T. Japan, Inc. carries: ['MOCHI ICE CREAM BONBONS']", response.data)
    
    def test_display_products_fail(self):
        response = self.app.get('/getAllProducts/random brand', follow_redirects=True)
        self.assertEqual(b'random brand carries: None', response.data)
    
    def test_display_ingredients_success(self):
        response = self.app.get('/getProductIngredients/FRESH & EASY/DICED TOMATOES', follow_redirects=True)
        self.assertEqual(b'DICED TOMATOES from FRESH & EASY contains: tomatoes, tomato, juice, calcium chloride, citric acid.', response.data)

if __name__ == '__main__':
    unittest.main()