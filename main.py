

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

'''

Tables:

1. gmailacc
2. socialmediaacc
3. Working on IT

'''

#gmailacc_MANAGEMENT_PROGRAMandFUNCTIONS

def GMAILACC():

    print()
    print('< Welcome to your GMAIL ACCOUNT MANAGEMENT DATABASE >\n')


    def insertData():  


        print('Kindly Insert data related to your gmail accounts:')
        print()

        choice = 'y'
        while (choice.lower() == 'y'):

            sno = int(input('Enter Proper Serial Number:'))
            acc = input('Enter GMAIL ACCOUNT:')
            passwd = input(f"Enter PASSWORD for {acc}:")
            extra = input('Enter Some extra info you want to give:')

            query = "insert into gmailacc(Sno,Gmail_Account,Password,Extra_info) values({},'{}','{}','{}')".format(sno,acc,passwd,extra)
            
            myCursor.execute(query)
            myConnection.commit()

            choice = input('Want to enter more data(y/n):')
            print()

    def allGmailaccData():

        myCursor.execute("select * from gmailacc")
        data = myCursor.fetchall()

        for i in data:
            print(i)
            print()

    
    def UpdatePassword_gmailacc():

        
        
        
        myCursor.execute("select * from gmailacc")
        data = myCursor.fetchall()

        for j in data:

            print(j)
            print()
        print()

        print('< Please select the Gmail Account of which you are updating your Password >')
        print()

        

        askSno = int(input('Enter the Sno:'))
        
        newPassword = input('Enter the new Password:')

        
        query = "update gmailacc set Password = '{}' where Sno = {}".format(newPassword,askSno)

        myCursor.execute(query)
        myConnection.commit()

        print()


    def removeData():

        myCursor.execute("select * from gmailacc")
        data = myCursor.fetchall()
        for a in data:
            print(a)
            print()


        print()
        print("Please select the Gmail Account which you want to delete:")
        print()


        sno = int(input('Enter Sno:'))

        query = "DELETE FROM gmailacc WHERE Sno = {}".format(sno)
        myCursor.execute(query)
        myConnection.commit()
    

        print('Data Removed!')
        print()

    
    def updateExtra_gmailacc():


        print()
        askSnoforExtra = int(input("Enter the Account's Sno for which you want to give some extra Information:"))



        print()
        print("< Give some Extra Information you want to give for the respective Account >")
        print()


        askInfo = input('Write Here:')

        query = "update gmailacc set Extra_info = '{}' where Sno = {}".format(askInfo,askSnoforExtra)

        myCursor.execute(query)
        myConnection.commit()
    

    def searchgmailacc():

        print()
        searchInput = input('TYPE GMAIL NAME:')
        print()

        query = "select * from gmailacc where Gmail_Account like '{}%'".format(searchInput)

        myCursor.execute(query)
        data = myCursor.fetchall()


        print("Sno , GmailAccount , Password , ExtraInfo")

        for i in data:

            print(i)
            print()



    #MenuDrive_FOR_GMAILACC_
                
            
    while True:
        print()
    
        optionsLST = ['1-> Insert Data' , '2-> Show complete data for GMAIL ACCOUNT' , '3-> Update Gmail Account Password' , '4-> Remove Data' , '5-> Give Some Extra Info for the respective account' , '6-> Search GMAIL Account' , '7-> Exit']

        for options in optionsLST:
            print(options)

        print()
        gmailaccChoice = input('YOUR CHOICE:')
        print()

        if (gmailaccChoice.isdigit()):

            if (int(gmailaccChoice) == 1):

                insertData()
            
            elif (int(gmailaccChoice) == 2):

                print("Sno , GmailAccount , Password , ExtraInfo")

                allGmailaccData()

            elif (int(gmailaccChoice) == 3):

                UpdatePassword_gmailacc()


            elif (int(gmailaccChoice) == 4):

                removeData()


            elif (int(gmailaccChoice) == 5):

                updateExtra_gmailacc()


            elif (int(gmailaccChoice) == 6):
                searchgmailacc()


            elif (int(gmailaccChoice) == 7): #exit

                break
        
        else:

            print("Invalid Input, Try Again!")
            break



#MAIN_MENU_DRIVE
            

while True:


    print()

    optionsLST = ['1-> GMAIL_ACCOUNT' , '2-> EXIT']

    for options in optionsLST:
        print(options)

    print()

    tableChoice = input('CHOOSE AND ACCESS THE TABLE:')


    if (tableChoice.isdigit()):

        if (int(tableChoice) == 1):

            GMAILACC()

        if (int(tableChoice) == 2): #EXIT

            print()
            print('Program Closed Successfully!')
    
            break

        
    else:
        print('Invalid Input, Try Again...!!')
        break

