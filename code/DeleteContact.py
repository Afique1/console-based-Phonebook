from code import contact
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
