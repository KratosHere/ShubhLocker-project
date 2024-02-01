
import pickle

with open("MySQLpassword.dat",'wb') as f:

    askPasswd = input('Enter Password for your MySQL:')

    pickle.dump(askPasswd,f)

    