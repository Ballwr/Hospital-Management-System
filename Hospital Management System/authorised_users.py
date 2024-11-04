# Setup file to add new authorized users with hashed passwords
import mysql.connector as my
import bcrypt

def add_authorized_user(username, password):
    mycon = my.connect(
        host='localhost',
        user='root',
        passwd='admin',
        database='hospital'
    )
    cursor = mycon.cursor()

    # Hash the password
    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    # Insert user into the authorized_users table
    query = "INSERT INTO authorized_users (username, password_hash) VALUES (%s, %s)"
    data = (username, password_hash)
    cursor.execute(query, data)
    mycon.commit()
    cursor.close()
    mycon.close()
    print("Authorized user added successfully.")
