# importing the psycopg2 module
import psycopg2

class dbService():
    database = 'myduka'
    user = 'postgres'
    password = 'Mamamia11'

    def __init__(self):
        self.database='myduka'
        self.user='postgres'
        self.password='Mamamia11'
        self.connection = psycopg2.connect(database=self.database, user=self.user, password=self.password)
        self.cursor = self.connection.cursor()
        pass

    def get_data(self, table):
        # database = 'myduka'
        # user = 'postgres'
        # password = 'Mamamia11'

        # connecting to the database
        # connection = psycopg2.connect(database=self.database, user=self.user, password=self.password)

        # instantiating the cursor
        # cursor = self.connection.cursor()

        # query to select a table
        fetch_all = "SELECT * FROM "+table
        self.cursor.execute(fetch_all)

        # fetching all the rows
        rows = self.cursor.fetchall()
        return(rows)
        

    def addProduct(self, id, name, buying_price, selling_price, stock_quantity):
        insert = f"INSERT INTO products (name, buying_price, selling_price, stock_quantity) VALUES ( '{name}', {buying_price}, {selling_price}, {stock_quantity})"
        
        #execute the query 
        self.cursor.execute(insert)

        # saving the changes to the database
        self.connection.commit()
        return "success"


    def addSale(self, id, pid, quantity):
        insert = f"INSERT INTO sales (pid, quantity) VALUES ( {pid}, {quantity})"
        
        #execute the query 
        self.cursor.execute(insert)

        # saving the changes to the database
        self.connection.commit()
        return "success"
        pass

    def remaining_stock(self):
#         "SELECT p.name, (p.stock_quantity - (SUM(s.quantity))) rem_stock
    # FROM sales s
#   JOIN products p ON p.product_id = s.product_id 
#   GROUP BY product_id;"

        query = "SELECT p.id, p.name, (p.stock_quantity - SUM(s.quantity)) as qty FROM sales s JOIN products p on p.id=s.pid WHERE (p.stock_quantity - s.quantity) > 0 GROUP BY p.id"
        self.cursor.execute(query)

        # fetching all the rows
        rows = self.cursor.fetchall()
        return(rows)
        pass

service= dbService()
print(service.remaining_stock())
data=service.get_data(input("Enter Table Name:"))
print(str(data))

addProduct = service.addProduct(input("Enter ID:"), input("Enter Name:"), input("Enter Buying price:"), input("Enter Selling price:"), input("Enter Stock Quantity:"))
print(addProduct)

newSale = service.addSale(input("Enter ID:"), input("Enter Product ID:"), input("Enter Quantity:"))
print(newSale)

# storing all the information
# database = 'myduka'
# user = 'postgres'
# password = 'Mamamia11'

# # connecting to the database
# connection = psycopg2.connect(database=database, user=user, password=password)

# # instantiating the cursor
# cursor = connection.cursor()

# # query to create a table
# fetch_all = "SELECT * FROM products"
# cursor.execute(fetch_all)

# # fetching all the rows
# rows = cursor.fetchall()
# print(rows)
# # printing the data
# # for row in rows:
# #     print(f"{row[0]} {row[1]}")
#     # closing the connection
# connection.close()

