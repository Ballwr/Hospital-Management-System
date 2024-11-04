import mysql.connector as my
from patientrecord import access_patient_records, fill_patient_form
from staffrecord import access_staff_records, fill_staff_form

mycon = my.connect(
    host='localhost', 
    user='root', 
    passwd='admin', 
    database='hospital'
)

if mycon.is_connected():
    print("Connection Successful")
else:
    print("Connection Error")

print("Welcome to Pandurang Hospital")
print("Choose Action:")
print("1. See Patient Records", "2. Fill Patient Form", "3. See Staff Records", "4. Fill Staff Form")
user_input = int(input("Enter number: "))

if user_input == 1:
    access_patient_records()
elif user_input == 2:
    fill_patient_form()
elif user_input == 3:
    access_staff_records()
elif user_input==4:
    fill_staff_form()
else:
    print("No such option!")

mycon.close()
