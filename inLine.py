import mysql.connector
import datetime

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="inline"
)

mycursor = mydb.cursor()

def createCustomer(phone_num, email, name, zipcode):
    sql = "INSERT INTO customers (phone_num, email, name, zipcode) VALUES (%s, %s, %s, %s)"
    val = (phone_num, email, name, zipcode)
    mycursor.execute(sql, val)
    mydb.commit()

# createCustomer("4404658021", "jeffreykozik@protonmail.com", "Jeffrey Kozik", "44133")
# createCustomer("9782045866", "winikiwang@gmail.com", "Niki Wang", "44106")

def createBusiness(phone_num, email, name, zipcode):
    sql = "INSERT INTO businesses (phone_num, email, name, zipcode) VALUES (%s, %s, %s, %s)"
    val = (phone_num, email, name, zipcode)
    mycursor.execute(sql, val)
    mydb.commit()

# createBusiness("2167952355", None, "Mia Bella", "44106")

def createService(service_name, business_phone_num):
    sql = "INSERT INTO services (service_name, business_phone_num) VALUES (%s, %s)"
    val = (service_name, business_phone_num)
    mycursor.execute(sql, val)
    mydb.commit()

# createService("Dinner", "2167952355")

def getInLine(service_name, business_phone_num, customer_phone_num):
    mycursor.execute("SELECT count(*) FROM inline")
    people_in_line = mycursor.fetchone()[0]
    print(people_in_line)
    sql = "INSERT INTO inline (service_name, business_phone_num, customer_phone_num, position, minutes_left) VALUES (%s, %s, %s, %s, %s)"
    val = (service_name, business_phone_num, customer_phone_num, int(people_in_line) + 1, int(people_in_line)*5)
    mycursor.execute(sql, val)
    mydb.commit()

# getInLine("Dinner", "2167952355", "4404658021")
# getInLine("Dinner", "2167952355", "9782045866")

def getOutOfLine(service_name, business_phone_num, customer_phone_num):
    sql = "DELETE FROM inline WHERE customer_phone_num = '" + customer_phone_num + "' AND business_phone_num = '" + business_phone_num + "'"
    mycursor.execute(sql)
    mydb.commit()

# getOutOfLine("Dinner", "2167952355", "9782045866")

def removeNextFromLine(service_name, business_phone_num):
    mycursor.execute("SELECT customer_phone_num FROM inline WHERE position = 1 AND business_phone_num = '" + business_phone_num + "'")
    thisCustomerPhoneNum = mycursor.fetchone()[0]
    sql = "DELETE FROM inline WHERE position = 1 AND business_phone_num = '" + business_phone_num + "'"
    mycursor.execute(sql)
    sql = "INSERT INTO visits (customer_phone_num, business_phone_num, visit_date) VALUES (%s, %s, %s)"
    val = (thisCustomerPhoneNum, business_phone_num, datetime.datetime.now())
    mycursor.execute(sql, val)
    mydb.commit()

# removeNextFromLine("Dinner", "2167952355")

print(mycursor.rowcount, "record inserted.")
