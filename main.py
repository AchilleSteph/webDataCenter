from flask import Flask, render_template, request
from doctor import Account
from connection import create_schema, create_database, run_request
from signUp import write_doctor_file
# moi = Account('stachylle@yahoo.fr', '1234')
# print(moi)

app = Flask(__name__)

@app.route("/")
def signup():
    return render_template("doctorweb.html")

@app.route("/signIn")
def signin():
    return render_template("signIn.html")

@app.route("/signup")
def pageweb_preparation():
    return render_template("signup.html")

@app.route("/submit-signup", methods = ["POST"])
def submit():
    if request.method == "POST":
        # collect data from user keyboard (html page)
        first = request.form["doc_fname"].strip()
        last = request.form["doc_lname"].strip()
        gen = request.form["gender"]
        birth = request.form["birthday"]
        em = request.form["email"].strip()

        pwd = request.form["passwd"]
        #pwd2 = request.form["passwd-confirm"]
        #if pwd != pwd2: 
            #print("the second password is different form the first one. Try again !")

        
        # display data from Python to html page
        
        # create a datbase for a doctor who is just registered on the site
        create_database(create_schema(first, last))

        # save doctor's information in doctor_file.csv
        
        write_doctor_file(first, last, gen, birth, em, pwd)
        


    return render_template("submit-signup.html")
    #retrun render_template("submit-signup.html", f=first, l=last, g = gen, b = birth, e=em, p=pwd)



if __name__=="__main__":
    app.run(debug=True)

