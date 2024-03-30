from flask import Flask, render_template, request
from doctor import Account

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
        first = request.form["doc_fname"]
        last = request.form["doc_lname"]
        gen = request.form["gender"]
        birth = request.form["birthday"]
        em = request.form["email"]

        pwd = request.form["passwd"]
        #pwd2 = request.form["passwd-repeat"]
        #if pwd != pwd2: 
            #print("the second password is different form the first one. Try again !")


        # display data from Python to html page
    return render_template("submit-signup.html", f=first, l=last, g = gen, b = birth, e=em, p=pwd)

if __name__=="__main__":
    app.run(debug=True)

