####################################################
# PYTHON DB CONNECTION: connecting python code with DB
#
# why we need DB:
# - to store data permanently in DB. Ex- a gaming application
# - otherwise, we were using variables which lost data when application closes; even if storing in files, it's not structured, we can't perform query.
#
# Default MySQL port: 3306
# Default root user name: root
# MySQL Workbench - GUI
# MySQL Shell - Mysql cli
#
# - to connect MySQL db with python code, we need MySQL connector in between.
# - to install mysql connector:
#   * open cmd:
#       pip install mysql-connector-python
#       pip show mysql-connector-python     (version should be >8)
#
####################################################

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="Admin@1")     # connect() method return a db connection object
print("connection successful")

mycursor = mydb.cursor()        # cursor() method return the pointer for mydb connection to be able to work with your dbs

mycursor.execute("SHOW DATABASES")  # execute() method is used to execute any sql query

for i in mycursor:              # because mycursor holds all the data for the query you executed
    print(i)

'''
mydb = mysql.connector.connect(host="localhost", user='root', passwd='Admin@1', database="onlinelibrary")
print("connection successful")

mycursor = mydb.cursor()

mycursor.execute("select * from course")    # course is the table name in onlinelibrary db

# for i in mycursor:
#     print(i)

# OR

result = mycursor.fetchall()    # to fetch all records from mycursor
# result = mycursor.fetchone()    # to fetch only 1st record

print(result)               # returns a list of tuples(row data)
for i in result:
    print(i)                # printing list elements, each tuple
'''