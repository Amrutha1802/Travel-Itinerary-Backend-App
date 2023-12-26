import pymysql

# Creating my sql connection object
db_conn = pymysql.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="ItineraryDataBase",
)
