import pymysql

# Creating mysql connection object
db_conn2 = pymysql.connect(
    host="localhost",
    user="root",
    password='',
    database="ItineraryDataBase",
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
