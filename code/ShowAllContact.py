from code import contact
def ShowAllContact():
    print("\n---List of all contacts---\n")
    for key,value in contact.items():
        Name=value['Name']
        PhoneNo=value['PhoneNo']
        Address=value['Address']
        Email=value['Email']
        
        print(f'User name : {key}')
        print(f'\t Name : {Name}\n\t Phone No : {PhoneNo}\n\t Address : {Address}\n\t E-mail : {Email}')
