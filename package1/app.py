from flask import Flask, request, redirect, render_template, Blueprint,send_from_directory
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
    return render_template("index.html", y_pred=y_pred, Y_real= Y_real)

@app.route('/robots.txt')
def robot_to_root():
    return send_from_directory(app.static_folder, request.path[1:])
