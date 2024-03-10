from code import contact
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