import mysql.connector
from doctor import Account
from doctor import RegisterDoctor
import csv

mike = Account("Michael", "Tyson", "Male", "2024/01/25", "rrrrr@ttt", "0000")
print(mike)

# connect to mysql database

db = mysql.connector.connect(
    host = "localhost",
    user = "root", 
    password = "1234",
    database = "playersDB"
)

curseur = db.cursor()
curseur.execute("select * from personal_info")

# print information in the cursor
for x in curseur:
    print(x)
db.close()

# function to insert a doctor in the csv doctor's file
def write_doctor_file(fname, lname, gender, birth, username, password):
    doctor = Account(fname, lname, gender, birth, username, password)
    

    with open("doctor_file.csv", "a") as main_file:
        pencil = csv.writer(main_file, delimiter=";", quoting=csv.QUOTE_NONNUMERIC)
        pencil.writerow((doctor.fname, doctor.lname, doctor.gender, doctor.birth, doctor.username, doctor.password))
        
        main_file.close()



