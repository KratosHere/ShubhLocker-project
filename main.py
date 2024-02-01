

import mysql.connector as mysqlconnector
import pickle



def GENpasswd():

    with open("MySQLpassword.dat",'wb') as f:

        askPasswd = input('Enter Password for your MySQL:')

        pickle.dump(askPasswd,f)
    
GENpasswd()


with open('MySQLpassword.dat','rb') as f:

    MYpasswd = pickle.load(f)



myConnection = mysqlconnector.connect(host='localhost',user='root',passwd=MYpasswd,database='important_shubhdata')

myCursor = myConnection.cursor()

