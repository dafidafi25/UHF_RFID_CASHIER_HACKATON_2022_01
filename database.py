import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='cashier',
                                         user='cashier_admin',
                                         password='@cashier12345')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)

def checkDataFromDatabase(stock_uuid):
    cursor.execute("select * from stock_data where stock_uuid = '" + stock_uuid + "';")
    myresult = cursor.fetchall()

    print("Query", "select * from stock_data where stock_uuid ='" + stock_uuid + "';")

    if len(myresult) == 0:
        print("stock_uuid not Found")

    for x in myresult:
        print(x[0])
        print(x[1])
        print(x[2])
        print(x[3])

    return myresult
# finally:
#     if connection.is_connected():
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")
