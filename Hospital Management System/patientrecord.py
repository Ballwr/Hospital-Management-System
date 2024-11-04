import mysql.connector as my
import random
mycon = my.connect(host = 'localhost' , user = 'root' , passwd = 'admin' , database = 'hospital')
if mycon.is_connected() == True:
    print("Connection Successful")
else:
    print("Connection Error")

'''str = """create table patient (Patient_No int primary key , Patient_FName varchar(30) , Patient_LName varchar(30), Age int , address varchar(50) ,gender char(1))"""'''


def generate_patient_id():
    Patient_ID = random.randint(10000 , 99999)
    return Patient_ID

def access_patient_records():
    print("Choose Action: ")
    print('1. Update', '2. Delete', '3. See Patient Details')
    user_input = int(input("Enter a number: "))
    if user_input == 1:
        Patient_No = input("Enter Patient ID: ")
        patient_Fname = input("Enter Patient First Name: ")
        patient_Lname = input("Enter Patient Last Name: ")
        patient_age = int(input("Enter Staff Age: "))
        patient_gender = input("Enter Patient gender: ")
        patient_address = input("Enter Patient Address: ")
        patient_qualif = input("Enter Patient Disease: ")

        cursor = mycon.cursor()
        query = "INSERT INTO patient values(patient_id, patient_Fname, patient_Lname, patient_age , patient_gender , patient_address , patient_qualif)"
        cursor.execute(query, (Patient_No, patient_Fname, patient_Lname, patient_age,patient_gender, patient_address, patient_qualif))
        mycon.commit()
        cursor.close()
        print("Patient record updated successfully.")
    elif user_input == 2:
        user_input = int(input("Enter patient_ID: "))
        cursor = mycon.cursor()
        query = "DELETE FROM patient WHERE Patient_No = %s"
        cursor.execute(query, (user_input,))
        mycon.commit()
        cursor.close()
        print("Patient record deleted successfully.")
    else:
        cursor = mycon.cursor()
        query = "SELECT * FROM patient" 
        cursor.execute(query)
        results = cursor.fetchall()
        for record in results:
            print(record)
            cursor.close()


def fill_patient_form():
    cursor = mycon.cursor()

    Patient_No = generate_patient_id()
    Fname = input("Enter patient Fname: ")
    Lname = input("Enter patient Lname: ")
    age = int(input("Enter patient age: "))
    address = input("Enter patient address: ")
    gender = input("Enter gender: ")
    disease = input("Enter disease: ")

    str = 'insert into patient values(%s, %s, %s, %s, %s, %s, %s)'
    data = (Patient_No, Fname, Lname, age, address, gender, disease)
    try:
        cursor.execute(str , data)
        mycon.commit()
        print("Staff details successfully added")
    except Exception as e:
        mycon.rollback()
        print("Failed to enter details into the database")
        print("Error: ", e)