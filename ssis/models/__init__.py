import mysql.connector as mysql
from os import getenv

db = mysql.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'ssisdb'
        )
cursor = db.cursor()



