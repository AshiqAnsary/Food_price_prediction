
from distutils.debug import DEBUG
from urllib import request
from flask import Flask, render_template, request
import numpy as np
import sklearn
import pickle

app = Flask(__name__)

model=pickle.load(open("linear_model.pkl","rb"))


@app.route("/",methods=["GET","POST"])
def index():
    return render_template("index.html")


@app.route("/prediction",methods=["POST"])
def prediction():

    if request.method=="POST":
        Market=request.form["Market"]
        Category=request.form["Category"]
        Commodity=request.form["Commodity"]
        PriceType=request.form["PriceType"]
        Year=request.form["Year"]
        Month=request.form["Month"]
        

        predict=model.predict([[Market,Category,Commodity,PriceType,Year,Month]])
        return render_template("index.html",predict="Price is{}".format(predict))
    else:

            return render_template("index.html",predict="Not predictable")
        


if __name__ == "__main__":
    app.run(debug=True)
