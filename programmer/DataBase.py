from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host = 'localhost',
        user = 'root',
        password = 'Jkbvg!18'
    ) as connection:
        print(connection)
except Error as e:
    print(e)