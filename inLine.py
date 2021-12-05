import mysql.connector
import datetime
import random

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
    mycursor.execute("SELECT count(*) FROM inline WHERE business_phone_num = '" + business_phone_num + "' AND service_name = '" + service_name + "'")
    people_in_line = mycursor.fetchone()[0]
    print(people_in_line)
    sql = "INSERT INTO inline (service_name, business_phone_num, customer_phone_num, position, minutes_left) VALUES (%s, %s, %s, %s, %s)"
    val = (service_name, business_phone_num, customer_phone_num, int(people_in_line) + 1, 5 + int(people_in_line)*5)
    mycursor.execute(sql, val)
    mydb.commit()

# getInLine("Dinner", "2167952355", "4404658021")
# getInLine("Dinner", "2167952355", "9782045866")

def getOutOfLine(service_name, business_phone_num, customer_phone_num):
    sql = "SELECT position FROM inline WHERE customer_phone_num = '" + customer_phone_num + "' AND business_phone_num = '" + business_phone_num + "'" + " AND service_name = '" + service_name + "'"
    mycursor.execute(sql)
    thisCustomerPosition = mycursor.fetchone()[0]
    sql = "DELETE FROM inline WHERE customer_phone_num = '" + customer_phone_num + "' AND business_phone_num = '" + business_phone_num + "'" + " AND service_name = '" + service_name + "'"
    mycursor.execute(sql)
    mydb.commit()
    sql = "UPDATE inLine SET position = position - 1, minutes_left = minutes_left - 5 WHERE position > " + str(thisCustomerPosition)
    mycursor.execute(sql)
    mydb.commit()

# getOutOfLine("Dinner", "2167952355", "4404658021")

def removeNextFromLine(service_name, business_phone_num):
    mycursor.execute("SELECT customer_phone_num FROM inline WHERE position = 1 AND business_phone_num = '" + business_phone_num + "'" + " AND service_name = '" + service_name + "'")
    thisCustomerPhoneNum = mycursor.fetchone()[0]
    sql = "DELETE FROM inline WHERE position = 1 AND business_phone_num = '" + business_phone_num + "'" + " AND service_name = '" + service_name + "'"
    mycursor.execute(sql)
    sql = "INSERT INTO visits (customer_phone_num, business_phone_num, visit_date) VALUES (%s, %s, %s)"
    val = (thisCustomerPhoneNum, business_phone_num, datetime.datetime.now())
    mycursor.execute(sql, val)
    sql = "UPDATE inLine SET position = position - 1, minutes_left = minutes_left - 5"
    mycursor.execute(sql)
    mydb.commit()

removeNextFromLine("Dinner", "2167952355")

def createManyBusinesses(n):
    for i in range(n):
        randomPhoneNum = ""
        for j in range(10):
            randomPhoneNum += str(random.randrange(0, 9))
        randomZipCode = ""
        for k in range(5):
            randomZipCode += str(random.randrange(0,9))
        firstWord = ["Amazing", "Wonderful", "Tasty", "Yummy", "Delicious", "Fantastic", "Quaint", "Superb", "Trendy", "Hidden"]
        secondWord = ["Red", "Blue", "Orange", "Yellow", "Green", "Indigo", "Violet", "Pink", "Purple"]
        thirdWord = ["Italian", "Mexican", "Chinese", "Japanese", "American", "French", "Middle Eastern", "Russian", "Australian", "African"]
        fourthWord = ["Restaurant", "Bakery", "Breakfast Place", "Lunch Place", "Dinner Place"]
        randomName = random.choice(firstWord) + " " + random.choice(secondWord) + " " + random.choice(thirdWord) + " " + random.choice(fourthWord)
        createBusiness(randomPhoneNum, None, randomName, randomZipCode)
        # services = ["Outside", "Inside"]
        # service = random.choice(services)
        # createService(randomPhoneNum, service)

# createManyBusinesses(100)

def createManyCustomers(n):
    for i in range(n):
        randomPhoneNum = ""
        for j in range(10):
            randomPhoneNum += str(random.randrange(0, 9))
        randomZipCode = ""
        for k in range(5):
            randomZipCode += str(random.randrange(0,9))
        firstWord = ["Jeff", "Joshua", "Niki", "Remy", "Jasper", "Mike", "Nick", "Skye", "Simmons"]
        secondWord = ["Fitz", "Coulson", "Triplett", "Ward", "Nicholas", "George", "Amy"]
        thirdWord = ["Smith", "Johnson", "White", "Kozik", "Wang", "Love", "Garland", "Rubio", "Sexton"]
        randomName = random.choice(firstWord) + " " + random.choice(secondWord) + " " + random.choice(thirdWord)
        createCustomer(randomPhoneNum, None, randomName, randomZipCode)

# createManyCustomers(100)

# def getManyPeopleInLine(n):
#     mycursor.execute("SELECT phone_num FROM customers")
#     allCustomers = mycursor.fetchall()
#     for i in range(n):
#         getInLine(random.choice(allCustomers), )

def getBusinessesInZipcode(zipcode):
    mycursor.execute("SELECT * FROM businesses WHERE zipcode = " + str(zipcode))
    thisCustomerPhoneNum = mycursor.fetchall()
    print(thisCustomerPhoneNum)

# getBusinessesInZipcode(24145)

def getCustomersInZipcode(zipcode):
    mycursor.execute("SELECT * FROM customers WHERE zipcode = " + str(zipcode))
    thisCustomerPhoneNum = mycursor.fetchall()
    print(thisCustomerPhoneNum)

# getCustomersInZipcode(26164)

# print(mycursor.rowcount, "record inserted.")
