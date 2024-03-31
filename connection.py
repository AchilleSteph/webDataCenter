import mysql.connector

# create a schema
def create_schema(first_name, last_name):
    schema = first_name + "_" + last_name
    return schema

# function create database
def create_database(schema):
    db = mysql.connector.connect(
    host = "localhost",
    user = "root", 
    password = "1234"
    )

    cur = db.cursor()
    cur.execute("CREATE DATABASE " + schema)
    
    # create a table Patient
    run_request(schema, 
                "CREATE TABLE Patient(name VARCHAR(50), \
                                      age smallint UNSIGNED, \
                                      personID int PRIMARY KEY AUTO_INCREMENT)")

    db.close()

# function to connect to schema and run request req
def run_request(schema, req):
    db = mysql.connector.connect(
    host = "localhost",
    user = "root", 
    password = "1234",
    database = schema
    )

    curseur = db.cursor()
    curseur.execute(req)

    db.close()

# check the new database
#create_database("achille")