import pymysql
from dotenv import load_dotenv
import os

load_dotenv()
# Creating mysql connection object
db_conn2 = pymysql.connect(
    host=os.getenv("DATABASE_HOST"),
    user=os.getenv("DATABASE_USER"),
    password=os.getenv("DATABASE_PASSWORD"),
    db=os.getenv("DATABASE_NAME"),
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
)
