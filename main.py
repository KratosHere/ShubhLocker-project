

import mysql.connector as mysqlconnector
import pickle

with open('MySQLpassword.dat','rb') as f:

    MYpasswd = pickle.load(f)



myConnection = mysqlconnector.connect(host='localhost',user='root',passwd=MYpasswd,database='important_shubhdata')

myCursor = myConnection.cursor()

