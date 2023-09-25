# importing the psycopg2 module
import psycopg2

class dbService():
    database = 'myduka'
    user = 'postgres'
    password = 'Mamamia11'

    def __init__(self):
        pass

    def get_data(table):
        database = 'myduka'
        user = 'postgres'
        password = 'Mamamia11'

        # connecting to the database
        connection = psycopg2.connect(database=database, user=user, password=password)

        # instantiating the cursor
        cursor = connection.cursor()

        # query to select a table
        fetch_all = "SELECT * FROM "+table
        cursor.execute(fetch_all)

        # fetching all the rows
        rows = cursor.fetchall()
        return(rows)
        pass


service= dbService
data=service.get_data(input("Enter Table Name:"))
print(data)


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

