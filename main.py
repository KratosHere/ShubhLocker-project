

import mysql.connector as mysqlconnector
import os

MYpasswd = input('Enter Your MySQL password:')


myConnection = mysqlconnector.connect(host='localhost',user='root',passwd=MYpasswd,database='important_shubhdata')

myCursor = myConnection.cursor()

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


    
    def selfQuery():

        print()
        print("< WRITE YOUR OWN QUERY >")


        askQuery = input('Enter your Query:')

        query = askQuery

        myCursor.execute(query)
        data = myCursor.fetchall()

        for i in data:

            print(i)





    #MenuDrive_FOR_GMAILACC_
                
            
    while True:
        print()
    
        optionsLST = ['1-> Insert Data' , '2-> Show complete data for GMAIL ACCOUNT' , '3-> Update Gmail Account Password' , '4-> Remove Data' , '5-> Give Some Extra Info for the respective account' , '6-> Search GMAIL Account', '7-> Write Your Query' , '8-> Exit']

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


            elif (int(gmailaccChoice) == 7):

                selfQuery()


            elif (int(gmailaccChoice) == 8): #exit
                
                os.system('cls')
                break
                
        
        else:

            print("Invalid Input, Try Again!")
            break



#socialmediaacc_MANAGEMENT_PROGRAMandFUNCTIONS


def SOCIALMEDIAACC():

    print()
    print('< Welcome to your SOCIAL MEDIA ACCOUNT MANAGEMENT DATABASE >\n')


    def insertData():

        print('Kindly Insert data related to your Social Media accounts:')
        print()

        choice = 'y'
        while (choice.lower() == 'y'):

            sno = int(input('Enter Proper Serial Number:'))
            socialAcc = input('Enter SOCIAL MEDIA ACCOUNT:')
            passwd = input(f"Enter PASSWORD for {socialAcc}:")
            extra = input('Enter Some extra info you want to give:')

            query = "insert into socialmediaacc(Sno,Social_Account,Password,Extra_info) values({},'{}','{}','{}')".format(sno,socialAcc,passwd,extra)
            
            myCursor.execute(query)
            myConnection.commit()

            choice = input('Want to enter more data(y/n):')
            print()


    def removeData():

        myCursor.execute("select * from socialmediaacc")
        data = myCursor.fetchall()
        for a in data:
            print(a)
            print()


        print()
        print("Please select the Social Media Account which you want to delete:")
        print()


        sno = int(input('Enter Sno:'))

        query = "DELETE FROM socialmediaacc WHERE Sno = {}".format(sno)
        myCursor.execute(query)
        myConnection.commit()
    

        print('Data Removed!')
        print()
    
    def allSocialaccData():

        myCursor.execute("select * from socialmediaacc")
        data = myCursor.fetchall()

        for i in data:
            print(i)
            print()


    def UpdatePassword_socialacc():

        
        
        
        myCursor.execute("select * from socialmediaacc")
        data = myCursor.fetchall()

        for j in data:

            print(j)
            print()
        print()

        print('< Please select the Social Media Account of which you are updating your Password >')
        print()

        

        askSno = int(input('Enter the Sno:'))
        
        newPassword = input('Enter the new Password:')

        
        query = "update socialmediaacc set Password = '{}' where Sno = {}".format(newPassword,askSno)

        myCursor.execute(query)
        myConnection.commit()

        print()


    def updateExtra_socialacc():


        print()
        askSnoforExtra = int(input("Enter the Account's Sno for which you want to give some extra Information:"))



        print()
        print("< Give some Extra Information you want to give for the respective Account >")
        print()


        askInfo = input('Write Here:')

        query = "update socialmediaacc set Extra_info = '{}' where Sno = {}".format(askInfo,askSnoforExtra)

        myCursor.execute(query)
        myConnection.commit()

    def searchsocialacc():

        print()
        searchInput = input('TYPE SOCIAL MEDIA NAME:')
        print()

        query = "select * from socialmediaacc where Social_Account like '{}%'".format(searchInput)

        myCursor.execute(query)
        data = myCursor.fetchall()


        print("Sno , SocialAccount , Password , ExtraInfo")

        for i in data:

            print(i)
            print()

    def selfQuery():

        print()
        print("< WRITE YOUR OWN QUERY >")


        askQuery = input('Enter your Query:')

        query = askQuery

        myCursor.execute(query)
        data = myCursor.fetchall()

        for i in data:

            print(i)




    #MenuDrive_for_socialMediaACC
        
    
    while True:
        print()
        
        optionsLST = ['1-> Insert Data' , '2-> Show complete data for SOCIAL MEDIA ACCOUNT' , '3-> Update Social Media Account Password' , '4-> Remove Data' , '5-> Give Some Extra Info for the respective account' , '6-> Search Social Media Account' , '7-> Write Your Query' , '8-> EXIT']

        for options in optionsLST:
            print(options)


        print()
        gmailaccChoice = input('YOUR CHOICE:')
        print()

        if (gmailaccChoice.isdigit()):

            if (int(gmailaccChoice) == 1):

                insertData()
            
            elif (int(gmailaccChoice) == 2):

                print("Sno , SocialAccount , Password , ExtraInfo")

                allSocialaccData()

            elif (int(gmailaccChoice) == 3):

                UpdatePassword_socialacc()


            elif (int(gmailaccChoice) == 4):

                removeData()


            elif (int(gmailaccChoice) == 5):

                updateExtra_socialacc()


            elif (int(gmailaccChoice) == 6):
                searchsocialacc()


            elif (int(gmailaccChoice) == 7):

                selfQuery()

            elif (int(gmailaccChoice) == 8): #exit
                
                os.system('cls')
                break
        
        else:

            print("Invalid Input, Try Again!")
            break


#otheracc_MANAGEMENT_PROGRAMandFUNCTIONS

def OTHERACCOUNT():

    print()
    print('< Welcome to your OTHER IMPORTANT ACCOUNTS MANAGEMENT DATABASE >\n')


    def insertData():

        print('Kindly Insert data related to your OTHER accounts:')
        print()

        choice = 'y'
        while (choice.lower() == 'y'):

            sno = int(input('Enter Proper Serial Number:'))
            otherAcc = input('Enter ACCOUNT NAME:')
            passwd = input(f"Enter PASSWORD for {otherAcc}:")
            extra = input('Enter Some extra info you want to give:')

            query = "insert into otheracc(Sno,Account_Name,Password,Extra_info) values({},'{}','{}','{}')".format(sno,otherAcc,passwd,extra)
            
            myCursor.execute(query)
            myConnection.commit()

            choice = input('Want to enter more data(y/n):')
            print()


    def removeData():

        myCursor.execute("select * from otheracc")
        data = myCursor.fetchall()
        for a in data:
            print(a)
            print()


        print()
        print("Please select the Account which you want to delete:")
        print()


        sno = int(input('Enter Sno:'))

        query = "DELETE FROM otheracc WHERE Sno = {}".format(sno)
        myCursor.execute(query)
        myConnection.commit()
    

        print('Data Removed!')
        print()
    
    def allOtheraccData():

        myCursor.execute("select * from otheracc")
        data = myCursor.fetchall()

        for i in data:
            print(i)
            print()


    def UpdatePassword_otheracc():

        
        
        
        myCursor.execute("select * from otheracc")
        data = myCursor.fetchall()

        for j in data:

            print(j)
            print()
        print()

        print('< Please select the Account of which you are updating your Password >')
        print()

        

        askSno = int(input('Enter the Sno:'))
        
        newPassword = input('Enter the new Password:')

        
        query = "update otheracc set Password = '{}' where Sno = {}".format(newPassword,askSno)

        myCursor.execute(query)
        myConnection.commit()

        print()


    def updateExtra_otheracc():


        print()
        askSnoforExtra = int(input("Enter the Account's Sno for which you want to give some extra Information:"))



        print()
        print("< Give some Extra Information you want to give for the respective Account >")
        print()


        askInfo = input('Write Here:')

        query = "update otheracc set Extra_info = '{}' where Sno = {}".format(askInfo,askSnoforExtra)

        myCursor.execute(query)
        myConnection.commit()

    def searchOtherAcc():

        print()
        searchInput = input('TYPE ACCOUNT NAME NAME:')
        print()

        query = "select * from otheracc where Account_Name like '{}%'".format(searchInput)

        myCursor.execute(query)
        data = myCursor.fetchall()


        print("Sno , AccountName , Password , ExtraInfo")

        for i in data:

            print(i)
            print()


    def selfQuery():

        print()
        print("< WRITE YOUR OWN QUERY >")


        askQuery = input('Enter your Query:')

        query = askQuery

        myCursor.execute(query)
        data = myCursor.fetchall()

        for i in data:

            print(i)

    #MenuDrive_for_otherAcc
        
    
    while True:
        print()
        
        optionsLST = ['1-> Insert Data' , '2-> Show complete data for OTHER ACCOUNTS' , "3-> Update Account's Password" , '4-> Remove Data' , '5-> Give Some Extra Info for the respective account' , '6-> Search Account' , '7-> Write Your Query' , '8-> EXIT']

        for options in optionsLST:
            print(options)


        print()
        gmailaccChoice = input('YOUR CHOICE:')
        print()

        if (gmailaccChoice.isdigit()):

            if (int(gmailaccChoice) == 1):

                insertData()
            
            elif (int(gmailaccChoice) == 2):

                print("Sno , OtherAccount , Password , ExtraInfo")

                allOtheraccData()

            elif (int(gmailaccChoice) == 3):

                UpdatePassword_otheracc()


            elif (int(gmailaccChoice) == 4):

                removeData()


            elif (int(gmailaccChoice) == 5):

                updateExtra_otheracc()


            elif (int(gmailaccChoice) == 6):
                searchOtherAcc()


            elif(int(gmailaccChoice) == 7):

                selfQuery()



            elif (int(gmailaccChoice) == 8): #exit

                os.system('cls')
                break
        
        else:

            print("Invalid Input, Try Again!")
            break



#MAIN_MENU_DRIVE
            

while True:


    print()

    optionsLST = ['1-> GMAIL_ACCOUNT' , '2-> SOCIAL_MEDIA_ACCOUNT' , '3-> OTHER_ACCOUNTS', '4-> EXIT']

    for options in optionsLST:
        print(options)

    print()

    tableChoice = input('CHOOSE AND ACCESS THE TABLE:')


    if (tableChoice.isdigit()):

        if (int(tableChoice) == 1):

            GMAILACC()

        elif (int(tableChoice) == 2):

            SOCIALMEDIAACC()

        elif (int(tableChoice) == 3):

            OTHERACCOUNT()

        elif (int(tableChoice) == 4): #exit

            print()
            print('Program Closed Successfully!')
    
            break

    else:
        print('Invalid Input, Try Again...!!')
        break