from code import contact

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
