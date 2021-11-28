from flask import Flask, render_template
import os

app=Flask(__name__)

#MENU

@app.route("/")
def accueil():
    return render_template("accueil.html")

@app.route("/exercices/")
def exercices():
    return render_template("exercices.html")

@app.route("/exercices/fr/")
def exercicesFR():
    return render_template("exercicesFR.html")

@app.route("/exercices/mt")
def exercicesMT():
    return render_template("b1.html")

@app.route("/exercices/us/")
def exercicesUS():
    return render_template("c1.html")

@app.route("/jeux/")
def jeux():
    return render_template("jeux.html")

@app.route("/plus/")
def plus():
    return render_template("plus.html")


#EXERCICES DE FRANCAIS

@app.route("/exercices/fr/a1/")
def sonsFR():
    return render_template("a1.html")

@app.route("/exercices/fr/a2/")
def qqoFR():
    return render_template("a2.html")

@app.route("/exercices/fr/a3/")
def vocabulaireFR():
    return render_template("a3.html")

@app.route("/exercices/fr/a4/")
def vcFR():
    return render_template("a4.html")

@app.route("/exercices/fr/a5/")
def miFR():
    return render_template("a5.html")

@app.route("/exercices/fr/a6/")
def mMFR():
    return render_template("a6.html")

@app.route("/exercices/fr/a7/")
def syllFR():
    return render_template("a7.html")


#EXERCICES DE MATH

@app.route("/exercices/maths/b1/")
def pdMT():
    return render_template("b1.html")

@app.route("/exercices/maths/b2/")
def pmMT():
    return render_template("b2.html")

@app.route("/exercices/maths/b3/")
def ordreMT():
    return render_template("b3.html")

@app.route("/exercices/maths/b4/")
def suiteMT():
    return render_template("b4.html")

@app.route("/exercices/maths/b5/")
def vocgeoMT():
    return render_template("b5.html")

#EXERCICES DE UNIVERS SOCIAL

@app.route("/exercices/maths/c1/")
def tempsUS():
    return render_template("c1.html")

@app.route("/exercices/maths/c2/")
def jrsemUS():
    return render_template("c2.html")

@app.route("/exercices/maths/c3/")
def moisanUS():
    return render_template("c3.html")

@app.route("/exercices/maths/c4/")
def difsaisUS():
    return render_template("c4.html")

@app.route("/exercices/maths/c5/")
def voctempsUS():
    return render_template("c5.html")

@app.route("/exercices/maths/c6/")
def frequUS():
    return render_template("c6.html")

if __name__=="__main__":
    app.run(debug=True)
