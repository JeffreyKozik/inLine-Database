from flask import Flask, render_template, request, redirect, url_for
import inLine
import mysql.connector
import datetime
import random

phone_num = ""
email = ""
name = ""
zipcode = ""

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="inline"
)

mycursor = mydb.cursor()

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route("/customer", methods=['POST', 'GET'])
def customer():
    if request.form.get('signinphonenum') == None:
        print("phone_num", request.form.get('phone_num'))
        print("email", request.form.get('email'))
        print('name', request.form.get('name'))
        print('zipcode', request.form.get('zipcode'))
        inLine.createCustomer(request.form.get('phone_num'), request.form.get('email'), request.form.get('name'), request.form.get('zipcode'))
        return render_template("user.html", phone_num = request.form.get('phone_num'), email = request.form.get('email'), name = request.form.get('name'), zipcode = request.form.get('zipcode'))
    else:
        mycursor.execute("SELECT email, name, zipcode FROM Customers WHERE phone_num = '" + request.form.get('signinphonenum') + "'")
        all = mycursor.fetchone()
        print("all", all)
        email = all[0]
        name = all[1]
        zipcode = all[2]
        print("email", email)
        print("name", name)
        print("zipcode", zipcode)
        return render_template("user.html", phone_num = request.form.get('signinphonenum'), email = email, name = name, zipcode = zipcode)

@app.route("/business", methods=['POST', 'GET'])
def business():
    if request.form.get('signinBusinessPhoneNum') == None:
        print("phone_num", request.form.get('businessPhoneNumber'))
        print("email", request.form.get('businessEmail'))
        print('name', request.form.get('businessName'))
        print('zipcode', request.form.get('businessZipcode'))
        inLine.createBusiness(request.form.get('businessPhoneNumber'), request.form.get('businessEmail'), request.form.get('businessName'), request.form.get('businessZipcode'))
        return render_template("business.html", phone_num = request.form.get('businessPhoneNumber'), email = request.form.get('businessEmail'), name = request.form.get('businessName'), zipcode = request.form.get('businessZipcode'))
    else:
        mycursor.execute("SELECT email, name, zipcode FROM Businesses WHERE phone_num = '" + request.form.get('signinBusinessPhoneNum') + "'")
        all = mycursor.fetchone()
        print("all", all)
        email = all[0]
        name = all[1]
        zipcode = all[2]
        print("email", email)
        print("name", name)
        print("zipcode", zipcode)
        return render_template("business.html", phone_num = request.form.get('signinBusinessPhoneNum'), email = email, name = name, zipcode = zipcode)

# @app.route("/service", methods=['POST', 'GET'])
# def service():
#     inLine.createService(request.form.get('phone_num'), request.form.get('email'), request.form.get('name'), request.form.get('zipcode'))
