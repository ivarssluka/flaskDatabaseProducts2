from flask import Flask
from flask import render_template
from DatabaseConnection import getData, addNewAlcohol, deleteAlcoholRecord
from flask import request
from flask import redirect

webPage = Flask(__name__)

@webPage.route("/alcohol/<int:id>", methods=['POST', 'GET'])
def oneAlcohol(id):
    totalPay=0
    query = "Select * from Alcohol where id =" + str(id) + ";"
    oneDrink = getData(query)[0]
    daudzums =0

    if request.method == "POST":
        daudzums = request.form["daudzums"]
        totalPay = int(daudzums) * oneDrink[4]

    daudzums = int(daudzums)
    return render_template("one_alcohol.html", oneDrink=oneDrink, totalPay=totalPay, daudzums=daudzums)


@webPage.route("/add_alcohol", methods=['POST', 'GET'])
def add_alcohol():
    if request.method =="POST":
        print("Add new drink to database")
        newAlcoName = request.form["name"]
        newAlcoURL = request.form["img_url"]
        newAlcoDegre = request.form["degre"]
        newAlcoPrice = request.form["price"]

        isDicount = 0
        if request.form.__contains__("discount"):
            isDicount=1

        #newIsDiscount = request.form["discount"]
        #checkbox....
        print(newAlcoName +" " + newAlcoURL +" " +newAlcoDegre + " "+newAlcoPrice +  " ", isDicount)

        addNewAlcohol(newAlcoName,newAlcoURL,newAlcoDegre, newAlcoPrice,  isDicount)
        return redirect("/alcohol")

    else:
        return render_template("add_alcohol.html")



@webPage.route("/alcohol", methods =['POST', 'GET'])
def alchocol():
    quvery = "Select * from Alcohol order by name;"
    if request.method == "POST":
        #delete alcohol from database!
        if request.form.__contains__("drinkID"):
            drinkIDToDelete = request.form["drinkID"]
            deleteAlcoholRecord(drinkIDToDelete)

        #Check for specifik drink
        if request.form.__contains__("find"):
            print("Drink to Find ", request.form["find"])
            quvery = "Select * from Alcohol where name like '%"+request.form["find"] +"%';"

    alcoData = getData(quvery)
    return render_template("alcohol.html", alcoData=alcoData)



@webPage.route("/")
def mainRoot():
    return render_template("index.html")


@webPage.route("/all_users")
def allUsers():
    query ="Select * from Users order by username;"
    userData = getData(query)
    #print(userData)
    return render_template("all_users.html", userData = userData)


@webPage.route("/log_in")
def logIn():
    return render_template("log_in.html")





if __name__ == "__main__":
    webPage.run(debug=True)