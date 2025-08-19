from flask import Flask
from flask import render_template, request, redirect
from DatabaseConnection import getData, addNeWAlcohol,deleteRecord

webPage = Flask(__name__)


@webPage.route("/alcohol/<int:id>", methods=["GET", "POST"])
def oneAlcohol(id):

    total_pay = 0
    daudzums = 0
    query = "Select * from Alcohol where id =" + str(id) + ";"
    oneDrink = getData(query)[0]
    if request.method == "POST":
        daudzums = request.form["daudzums"]
        total_pay = int(daudzums) * oneDrink[4]
    daudzums = int(daudzums)

    return render_template("one_alcohol.html", oneDrink=oneDrink, total_pay=total_pay, daudzums=daudzums)


@webPage.route("/alcohol", methods=["GET", "POST"])
def alchocol():
    if request.method == "POST":
        #delete
        drinkToDelete = request.form["drink_id"]
        deleteRecord(drinkToDelete)

    query = "Select * from Alcohol order by name;"
    alcoData = getData(query)
    return render_template("alcohol.html", alcoData=alcoData)


@webPage.route("/")
def mainRoot():
    return render_template("index.html")


@webPage.route("/add_alcohol", methods=["GET", "POST"])
def addAlcohol():
    if request.method == "POST":
        newAlcoName = request.form["name"]
        newAlcoUrl = request.form["img_url"]
        newAlcoAlcVol = request.form["alc_vol"]
        newAlcoPrice = request.form["price"]

        isDiscount = 0
        if request.form.__contains__("discount"):
            isDiscount = 1

        # newAlcoDiscount = request.form["discount"]
        print(newAlcoName + " " + newAlcoUrl + " " + newAlcoAlcVol + " " + newAlcoPrice + " ", isDiscount)
        addNeWAlcohol(newAlcoName, newAlcoUrl, newAlcoAlcVol, newAlcoPrice, isDiscount)
        return redirect("/alcohol")
    return render_template("add_alcohol.html")

if __name__ == "__main__":
    webPage.run(debug=True)
