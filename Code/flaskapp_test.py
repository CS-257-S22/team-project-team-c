from flaskapp import *
import unittest

traditional_hummus_ingredients = ['CHICKPEAS', 'WATER', 'SESAME TAHINI', 'CANOLA OLIVE OIL BLEND', 'SALT', 'CITRIC ACID', 'NATURAL FLAVOR', 'GARLIC', 'SPICES', 'POTASSIUM SORBATE AND SODIUM BENZOATE']

class TestTwoMainFunction(unittest.TestCase):
    def setUp(self):
        """Set an app to test functions
        Written by Kana"""
        self.app = app.test_client()

    def test_homepage(self):
        """Test if the homepage displays the correct messages
        Written by Kana"""
        response = self.app.get('/', follow_redirects=True)
        self.assertIn(b'Welcome! Browse 80,000+ branded foods and private label data provided by the food industry.', response.data)

    def test_display_products(self):
        """Test if the page displays all products
        Written by Kana"""
        response = self.app.post('/displayproducts', data={"brandSearch":"G. T. Japan, Inc."})
        self.assertIn(b'MOCHI ICE CREAM BONBONS', response.data)
    
    def test_display_ingredients(self):
        """Test if the page displays all ingredients
        Written by Kana"""
        response = self.app.post('/displayingredients', data={"product":"TRADITIONAL HUMMUS"})
        for ingredient in traditional_hummus_ingredients:
            ingredient = bytes(ingredient, 'UTF-8')
            self.assertIn(ingredient, response.data)

    def test_display_ingredients_404(self):
        """Test if the 404 error page is shown when the product input is invalid
        Written by Kana"""
        response = self.app.post('/displayingredients', data={"product":"RANDOM PRODUCT"})
        self.assertIn(b'Page Not Found', response.data)  
    
    def test_help(self):
        """Test if the page displays FAQ
        Written by Kana"""
        response = self.app.get('/help', follow_redirects=True)
        self.assertIn(b'Frequently Asked Questions', response.data)
    
    
    def test_help(self):
        """Test if the page displays a contact form
        Written by Kana"""
        response = self.app.get('/contact', follow_redirects=True)
        self.assertIn(b'Connect With Us', response.data)

if __name__ == '__main__':
    unittest.main()
