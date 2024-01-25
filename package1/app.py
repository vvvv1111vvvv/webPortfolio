from flask import Flask, request, redirect, render_template, Blueprint
from model.model import DB_Access
import pymysql
import csv
import sys,os
from config import config
db_access= DB_Access()
db_access.checkDB()
predict_KOSPI_fromDB, actual_KOSPI_fromDB=db_access.getFromDB()
y_pred = predict_KOSPI_fromDB
Y_real = actual_KOSPI_fromDB
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():

    return render_template("index2.html", y_pred=y_pred, Y_real= Y_real)
#if __name__ == '__main__':
#    app.run(port=5001, host ='0.0.0.0', debug=True)