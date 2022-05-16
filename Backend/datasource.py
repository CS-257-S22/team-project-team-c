import psycopg2
import psqlConfig as config

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
            #set up a cursor
            cursor = self.connection.cursor()
            #make the query using %s as a placeholder for the variable
            query = "SELECT product_name FROM productTable WHERE brand_name=%s"
            cursor.execute(query, (brandInput,))
            print(cursor.fetchall())
        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None

    def get_all_ingredients(self, productInput):
        """
        Method to request a query to get the ingredeints of the product a user inputs.
        Args:
            productInput (str): product name taken from user 
        """
        try:
            #set up a cursor
            cursor = self.connection.cursor()
            #make the query using %s as a placeholder for the variable
            query = "SELECT ingredients FROM productTable WHERE product_name=%s"
            cursor.execute(query, (productInput,))
            print(cursor.fetchall())
        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None
    
if __name__ == '__main__':
    my_source = DataSource()
    #get all the products carried by 'DCI Cheese Company, Inc.'
    my_source.get_all_products('DCI Cheese Company, Inc.')
    #get all the ingredients in 'MOCHI ICE CREAM BONBONS'
    my_source.get_all_ingredients('MOCHI ICE CREAM BONBONS')