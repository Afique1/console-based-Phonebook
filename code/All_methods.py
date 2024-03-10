contact={
        'AFIQUE':{'Name':'Afique Sadique','PhoneNo':'0184','Address':'ABC road','Email':'afi@mail.com'} , 
        'ANOTHER USER': {'Name':'Another Sadique','PhoneNo':'0284','Address':'XYZ road','Email':'another@mail.com'}
        }
def ShowAllContact():
    print("\n---List of all contacts---\n")
    for key,value in contact.items():
        Name=value['Name']
        PhoneNo=value['PhoneNo']
        Address=value['Address']
        Email=value['Email']
        
        print(f'User name : {key}')
        print(f'\t Name : {Name}\n\t Phone No : {PhoneNo}\n\t Address : {Address}\n\t E-mail : {Email}')

def AddContact():
    print('\n---Add a contact---')
    user_name_for_key=input('\tUser Name : ').upper()
    name=input('\tName : ')
    phoneNo=input('\tPhone Number : ')
    address=input('\tAddress : ')
    email=input('\tEmail : ').lower()

    contact[user_name_for_key]          ={} #creating empty dict for nesting in contact
    contact[user_name_for_key]['Name']  =name
    contact[user_name_for_key]['PhoneNo']=phoneNo
    contact[user_name_for_key]['Address']=address
    contact[user_name_for_key]['Email'] =email

    print('\tContact added in your contact list.\n')

def DeleteContact():
    """ Deletes by UserName(key).deletes the key and value of that perticular key in dictonary"""

    print("\n---Delete contact---")
    delete_user=input('\nName of the User to be deleted : ').upper()
    if delete_user in contact:
        print(f"{delete_user}'s informations:\n{contact[delete_user]}")
        confirm_delete=input(f"\nDo you want to delete {delete_user} from contact book? [yes/no] : ").lower()
        if confirm_delete=='y'or confirm_delete=='yes':
            contact.pop(delete_user)  #removed item can be stored in another txt file
            print(f'{delete_user} has been deleted!')
        elif confirm_delete=='n'or confirm_delete=='no':
            print("\nContact wasn't deleted from contact list!")
        else:
            print("Invalid input.\nNo contact deleted.\n")
    else:
        print(f"{delete_user} not found!")

    #if delete_user==contact[delete_user]:

def SearchContact():
    """Search by userName in the contact dict and displays the contact/User's informations"""

    print("\n---Search contact---")
    search_user=input("User Name : ").upper()
    if search_user in contact:
        Name=contact[search_user]['Name']
        PhoneNo=contact[search_user]['PhoneNo']
        Address=contact[search_user]['Address']
        Email=contact[search_user]['Email']

        print('\nSearched user infrmation--')
        print(f'User name : {search_user}')
        print(f'\t Name : {Name}\n\t Phone No : {PhoneNo}\n\t Address : {Address}\n\t E-mail : {Email}')
    else: #if a contact isnt in contact then option to add a new contact
        print(f"{search_user} isn't available in your contact!")
        add_new=input(f"Do you want to add a new contact? [yes/no] : ").lower()
        if add_new=='yes' or add_new=='y':
            AddContact()
        elif add_new=='no' or add_new=='n':
            print('\tClosing option to add new contact!')
        else:
            print('\n!!!Invalid Input!!!')
            print('\tClosing option to add new contact!')

def UpdateContact():
    """to edit a contact which is matched by UserName key"""

    print("\n---Edit a contact---")
    update_usersName=input('Search by User Name : ').upper()
    if update_usersName in contact: 
        print("\n^^^Edit contact's following informations^^^")       
        name=input('\tName : ')
        phoneNo=input('\tPhone Number : ')
        address=input('\tAddress : ')
        email=input('\tEmail : ').lower()

        contact[update_usersName]['Name']=name
        contact[update_usersName]['PhoneNo']=phoneNo
        contact[update_usersName]['Address']=address
        contact[update_usersName]['Email']=email

        print('\nInformation successfully updated :D\n')
    else:
        print(f"{update_usersName} isn't available in your contact!")