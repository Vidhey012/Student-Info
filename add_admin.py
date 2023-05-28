from werkzeug.security import generate_password_hash
import mysql.connector as mysql



class Admin():
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = generate_password_hash(password, 'sha256')
    
    def add(self):
        query = f'''
        INSERT INTO admin(username,password)
        VALUE ('{self.username}', '{self.password}')
        '''
        cursor.execute(query)
        db.commit()
        print('Admin added!')


if __name__ == '__main__':
    host = 'localhost'
    user = 'root'
    password = ''

    db = mysql.connect(
            host = host,
            user = user,
            password = password,
            database = 'ssisdb'
        )
    cursor = db.cursor()

    print('MySQL connection established!')
    print()
    username = 'vidhey'
    password = 'vidhey'
    Admin(username,password).add()
    