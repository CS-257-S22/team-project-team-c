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
    
    def get_all_products(self, brandInput):
        """
        Method to request a query to get the products carried by the brand a user inputs.
        Args:
            brandInput (str): brand name taken from user 
        """
        try:
            cursor = self.connection.cursor()
            query = "SELECT product_name FROM productTable WHERE brand_name=%s"
            cursor.execute(query, (brandInput,))
            record = []
            for item in cursor.fetchall():
                record.append(item[0]) #change a tuple to a list
            return record

        except Exception as e:
            print (errorMessage, e)
            return None

    def get_all_ingredients(self, productInput):
        """
        Method to request a query to get the ingredeints of the product a user inputs.
        Args:
            productInput (str): product name taken from user 
        """
        try:
            cursor = self.connection.cursor()
            query = "SELECT ingredients FROM productTable WHERE product_name=%s"
            cursor.execute(query, (productInput,))
            ingredientList = cursor.fetchall()[0][0].split(", ")
            return ingredientList
        except Exception as e:
            print (errorMessage, e)
            return None

    def get_brand_list(self):
        """ Return a list of all brands in the database"""
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT DISTINCT brand_name FROM productTable")
            brandList = []
            for brand in cursor.fetchall():
                brandList.append(brand[0])
            return brandList
        except Exception as e:
            print (errorMessage, e)
            return None

    def get_products_list(self):
        """ Return a list of all products in the database"""
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT product_name FROM productTable")
            productList = []
            for product in cursor.fetchall():
                productList.append(product[0])
            return productList
        except Exception as e:
            print (errorMessage, e)
            return None
    
if __name__ == '__main__':
    my_source = DataSource()
    #print(my_source.get_products_list())
    #print(my_source.get_brand_list())
    print(my_source.get_all_products('DCI Cheese Company, Inc.'))
    print(my_source.get_all_ingredients('MOCHI ICE CREAM BONBONS'))