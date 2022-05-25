import psycopg2
import psqlConfig as config

errorMessage = "Something went wrong when executing the query: "
class DataSource:
    def __init__(self):
        self.connection = self.connect()

    def connect(self):
        """ Connect to the PostgreSQL database server """
        try:
            connection = psycopg2.connect(database=config.database, user=config.user, password=config.password, host="localhost")

        except Exception as e:
            print("Connection error: ", e)
            exit()
        return connection
    
    def get_all_products_from_brand(self, brandInput):
        """
        Method to request a query to get all products carried by the brand a user inputs.
        Args:
            brandInput (str): brand name taken from user 
        """
        try:
            cursor = self.connection.cursor()
            query = "SELECT product_name FROM productTable WHERE brand_name=%s" 
            cursor.execute(query, (brandInput,)) #brand_name = brandInput
            rawProductsData = cursor.fetchall()
            productList = []
            for item in rawProductsData:
                productList.append(item[0]) #change a tuple into a list
            return productList

        except Exception as e:
            print (errorMessage, e)
            return None

    def get_all_ingredients_from_product(self, productInput):
        """
        Method to request a query to get all ingredeints in the product a user inputs.
        Args:
            productInput (str): product name taken from user 
        """
        try:
            cursor = self.connection.cursor()
            query = "SELECT ingredients FROM productTable WHERE product_name=%s"
            cursor.execute(query, (productInput,)) 
            rawIngredientsData = cursor.fetchall() #a string of all ingredients (splited by commas) in a tuple in a list
            ingredientList = rawIngredientsData[0][0].split(", ") #access the tuple inside the list, and then access the string inside the tuple, and turn it into a list by splitting it with commas
            return ingredientList
        except Exception as e:
            print (errorMessage, e)
            return None

    def get_brand_list(self):
        """ Return a list of all brands in the database"""
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT DISTINCT brand_name FROM productTable")
            rawBrandData = cursor.fetchall()
            brandList = []
            for brand in rawBrandData:
                brandList.append(brand[0]) #turn it into a list
            return brandList

        except Exception as e:
            print (errorMessage, e)
            return None

    def get_products_list(self):
        """ Return a list of all products in the database"""
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT product_name FROM productTable")
            rawProductsData = cursor.fetchall()
            productList = []
            for product in rawProductsData:
                productList.append(product[0]) #turn it into a list
            return productList

        except Exception as e:
            print (errorMessage, e)
            return None
    
if __name__ == '__main__':
    my_source = DataSource()
    # print(my_source.get_products_list())
    # print(my_source.get_brand_list())
    # print(my_source.get_all_products_from_brand('Target Stores'))
    # print(my_source.get_all_ingredients_from_product('MOCHI ICE CREAM BONBONS'))