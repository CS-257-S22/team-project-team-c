import unittest
from webbrowser import get
from what2Eat import *

sampleData = what2Eat("SmallProductSheet.csv")
class TestIngredient(unittest.TestCase):
    def test_load_csv_file(self):
        result = sampleData.load_csv_file()
        ifNested = any(isinstance(row, list) for row in result)
        self.assertTrue(ifNested)

    def test_returnBrands(self):
        result = sampleData.returnBrands()
        brandList = ['G. T. Japan, Inc.', 'FRESH & EASY', "McConnell's Ice Cream Inc.",
         'Stater Bros. Markets Inc.', 'Meijer, Inc.', 'Target Stores', 
         'Milton G. Waldbaum Company', 'Columbus Manufacturing, Inc.', 
         'DCI Cheese Company, Inc.', 'FRESH&EASY', 'FRESH & TASTY', 
         'FRESH & EASY NEIGHBORHOOD MARKET INC.', 'FRESH & EASY ORGANIC']
        self.assertEqual(result, brandList)

    def test_isValidBrand_True(self):
        result = sampleData.isValidBrand("FRESH & EASY")
        self.assertTrue(result)

    def test_isValidBrand_False(self):
        result = sampleData.isValidBrand("FRESH OR EASY")
        self.assertFalse(result)

    def test_isValidBrand_blank(self):
        result = sampleData.isValidBrand("")
        self.assertFalse(result)

    def test_getAllProducts(self):
        result = sampleData.getAllProducts("Stater Bros. Markets Inc.")
        allProducts = ['STATER BROS., SUGAR POWDERED','STATER BROS., PURE CANE SUGAR GRANULATED',
                       'STATER BROS., ROTINI AN ENRICHED MACARONI PRODUCT',
                       'STATER BROS., KIDNEY BEANS, DARK RED']
        self.assertEqual(result, allProducts)

    def test_getProductIngredients(self):
            result = sampleData.getProductIngredients("FRESH & EASY", "BARBECUE SAUCE")
            allIngredients = "tomato puree (water, tomato paste), sugar, distilled vinegar, molasses, water, modified corn starch, salt, bourbon whiskey, contains 1% or less of: mustard flour, spice, dried onion, dried garlic, natural flavor, xanthan gum, caramel color."
            self.assertEqual(result, allIngredients)

    def test_containIngredients(self):
            result = sampleData.containsIngredient("molasses", "FRESH & EASY", "BARBECUE SAUCE")
            self.assertTrue(result)
    
    def test_containIngredients_FalseIngredients(self):
            result = sampleData.containsIngredient("random product", "FRESH & EASY", "BARBECUE SAUCE")
            self.assertFalse(result)
    
    def test_containIngredients_FalseBrand(self):
            result = sampleData.containsIngredient("molasses", "Random Brand", "BARBECUE SAUCE")
            self.assertFalse(result)
    
    def test_containIngredients_FalseProduct(self):
            result = sampleData.containsIngredient("molasses", "FRESH & EASY", "Random Product")
            self.assertFalse(result)

    def test_brandCarriesProduct_True(self):
        result = sampleData.brandCarriesProduct('FRESH & EASY', 'BARBECUE SAUCE')
        self.assertTrue(result)

    def test_brandCarriesProduct_FalseBrand(self):
        result = sampleData.brandCarriesProduct('Random Brand', 'BARBECUE SAUCE')
        self.assertFalse(result)
    
    def test_brandCarriesProduct_FalseProduct(self):
        result = sampleData.brandCarriesProduct('FRESH & EASY', 'Random Product')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
