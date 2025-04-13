contacts = {}           #creating empty dictionay

while True:
    print("\n----CONTACT BOOK----")
    print("1. Add contact")
    print("2. Update Contact")
    print("3. View all contacts")                                #creating a menu using WHILE TRUE loop 
    print("4. Delete contact")                              #to infinitely use book until user choose exit
    print("5. Exit")

    choice=input("Enter choice :  ")

                                                            #handling users choice with if-elif (inside while loop)

    if choice =='1':
        name=input("Enter Contact Name : ")
        number=input("Enter Contact Number : ")
        contacts[name]=number
        print("Contact Added! ")

    elif choice == '2':
        name=input("Enter contact name to update its number : ")    #updates the contact number
        if name in contacts:
            number=input("Enter The new number : ")
            contacts[name]=number
            print("Contact updated")
        else:
            print("Contact not found")
        
    elif choice == '3':
        for name,number in contacts.items():
            print(f"{name},{number}")

    elif choice=='4':
        delname=input("Enter Name of contact to delete :  ")    #if name is in contact condition is True and it will pop contact
        if name in contacts:
            contacts.pop(delname)
            #print("Contact Deleted")
            print(f"Contact '{delname}' Deleted! ")         #Displays The Deleted Contact Name
        else:
            print("Contact not found!!!")

    elif choice == '5':                                         #breaks and End the loop
        print("Exiting Contact Book...")
        break

    else:
        print("INVALID CHOICE!!!, Try Again.")

