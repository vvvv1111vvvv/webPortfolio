from flask import Flask, request, redirect, render_template, Blueprint
import pymysql
from model import DB_Access
import csv
import sys,os
import config

app = Flask(__name__)

db_access= DB_Access()
db_access.checkDB()

@app.route('/', methods=['GET','POST'])
def index():
    predict_KOSPI_fromDB, actual_KOSPI_fromDB=db_access.getFromDB()
    return render_template("index.html", y_pred = predict_KOSPI_fromDB, Y_real = actual_KOSPI_fromDB)

#if __name__ == '__main__':
#    app.run(port=5001, host ='0.0.0.0', debug=True)