import mysql.connector as my
import bcrypt
import random

mycon = my.connect(host='localhost', user='root', passwd='admin', database='hospital')
if mycon.is_connected():
    print("Connection Successful")
else:
    print("Connection Error")

cursor = mycon.cursor()
username = "admin-auth001"
password = "admin-password002"

def authenticate_user(username, password):
    cursor = mycon.cursor()
    
    # Query to get the stored password hash for the given username
    query = "SELECT password_hash FROM authorized_users WHERE username = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    cursor.close()

    if result:
        stored_password_hash = result[0]
        if bcrypt.checkpw(password.encode(), stored_password_hash.encode()):
            print("Authentication successful.")
            return True
        else:
            print("Incorrect password.")
    else:
        print("Username not found.")
    
    return False

    

def generate_staff_id():
    Staff_No = random.randint(10000 , 99999)
    return Staff_No


def access_staff_records():
    print("Choose an Action: ")
    print('1. Update', '2. Delete', '3. See Staff Details')
    user_input = int(input("Enter a number: "))
    
    if user_input == 1:
        user = input("Enter username: ")
        passwd = input("Enter password: ")
        if user == username and passwd == password:
            staff_id = input("Enter Staff ID: ")
            staff_Fname = input("Enter Staff First Name: ")
            staff_Lname = input("Enter Staff Last Name: ")
            staff_age = int(input("Enter Staff Age: "))
            staff_gender = input("Enter staff gender: ")
            staff_address = input("Enter Staff Address: ")
            staff_qualif = input("Enter Staff Qualifications: ")

            cursor = mycon.cursor()
            query = "INSERT INTO staff values(staff_ID, staff_Fname, staff_Lname, staff_age , staff_gender , staff_address , staff_qualif)"
            cursor.execute(query, (staff_id, staff_Fname, staff_Lname, staff_age,staff_gender, staff_address, staff_qualif))
            mycon.commit()
            cursor.close()
            print("Staff record updated successfully.")
    elif user_input == 2:
        user_input = int(input("Enter Staff_ID: "))
        cursor = mycon.cursor()
        query = "DELETE FROM staff WHERE staff_ID = %s"
        cursor.execute(query, (user_input,))
        mycon.commit()
        cursor.close()
        print("Staff record deleted successfully.")
    elif user_input == 3:
        cursor = mycon.cursor()
        query = "SELECT * FROM staff" 
        cursor.execute(query)
        results = cursor.fetchall()
        for record in results:
            print(record)
            cursor.close()
    else:
        print("Access denied. Unauthorized personnel.")

def fill_staff_form():
    cursor = mycon.cursor()
    Staff_ID = generate_staff_id()
    Fname = input("Enter Staff Fname: ")
    Lname = input("Enter Staff Lname: ")
    age = int(input("Enter Staff age: "))
    gender = input("Enter gender: ")
    address = input("Enter Staff address: ")
    qualif = input("Enter qualifications: ")

    str = 'insert into staff values(%s, %s, %s, %s, %s, %s, %s)'
    data = (Staff_ID, Fname, Lname, age, address, gender, qualif)
    try:
        cursor.execute(str , data)
        mycon.commit()
        print("Staff details successfully added")
    except Exception as e:
        mycon.rollback()
        print("Failed to enter details into the database")
        print("Error: ", e)

# Predefined authorized users with their passwords
authorized_users = {
    "admin": bcrypt.hashpw(b"admin-staff", bcrypt.gensalt()), # Replace with real password
    "manager": bcrypt.hashpw(b"admin-password001", bcrypt.gensalt()) # Replace with real password
}

def authenticate_user(username, password):
    """Function to check if the username and password are correct."""
    if username in authorized_users:
        # Check if the entered password matches the stored hashed password
        return bcrypt.checkpw(password.encode(), authorized_users[username])
    else:
        return False