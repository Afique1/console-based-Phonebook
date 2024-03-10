"""#allContact={'Name':'Afique','Address':'Abc road','Email':'afi@mail.com','phoneNo':'01845678910'}
allContact="Print this in file"
fileName='ContactList.txt'
with open(fileName,'a') as fileObject:
    fileObject.write(allContact)
with open(fileName) as fileObject:
    fileContent=fileObject.read()
print(fileContent)"""
import sys
from All_methods import AddContact,UpdateContact,DeleteContact,SearchContact,ShowAllContact,contact

print("________________________________________________\n\tYou've opend your contact book\n________________________________________________\n")

def Menu():
    print(" ----- ----- ----- ----- ----- ----- ----- ----- ")
    print("\t\tAvailable Option")
    print(" ----- ----- ----- ----- ----- ----- ----- ----- ")
    print("\t\t1. Add new \n\t\t2. Search \n\t\t3. Show all \n\t\t4. Edit \n\t\t5. Delete \n\t\t6. Quit Phonebook")
    print(" ----- ----- ----- ----- ----- ----- ----- ----- ")

continueOrQuit=''
def MenuOrQuit():
    continueOrQuit=input("Do you want to see Menu option or to quit? [menu/quit] : ").lower()
    if continueOrQuit=='menu' or continueOrQuit=='quit':
        if continueOrQuit=='menu':
            pass
        elif continueOrQuit=='quit':
            print('Quiting Application!')
            sys.exit()
            #break #code will stop executing
        else:
            print('\nInvalid option selected.\n\t')

    else:
        print('\nInvalid option selected\n')

while True:#continueOrQuit !='quit':
    try:
        Menu()
        
        option=input(" Select an option : ").lower()
        print(" ----- ----- ----- ----- ----- ----- ----- ----- ")

        if option=='1' or option=='add' or option=='add new':
            AddContact()
            MenuOrQuit()

        elif option=='2' or option=='search':
            SearchContact()
            MenuOrQuit()
        
        elif option=='3' or option=='show' or option == 'show all':
            if not contact: #empty dict
                print("No contact saved yet.")
            else:
                ShowAllContact()
                MenuOrQuit()
        
        elif option=='4' or option=='edit' or option=='update':
            UpdateContact()
            MenuOrQuit()
        
        elif option=='5' or option=='delete':
            DeleteContact()
            MenuOrQuit()


        elif option=='6' or option=='quit' or option=='q':
            print('Quiting Application!')
            break
        
        else:
            print('\nInvalid option selected\n\tTRY AGAIN!')
            MenuOrQuit()
    except:
        print('\nAn Unexcpted Error occured\n\tTRY AGAIN!')