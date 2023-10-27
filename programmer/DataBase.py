from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host = '62.76.220.88',
        user = 'root',
        password = 'Jkbvg!18'
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute('SHOW DATABASES')
            for db in cursor:
                print(db)
except Error as e:
    print(e)

