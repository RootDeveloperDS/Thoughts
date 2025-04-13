while True:
    print("\n1. Write a Note")               #Displaying MENU
    print("2. View Notes")                   #Infinite loop
    print("3. Exit.")

    choice=input("Enter Your Choice : ")     #Choice Handling
    if choice == '1':
        newnote()
    elif choice =='2':
        viewnote()
    elif choice =='3':
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try Again.")


def viewnote():                   #open notes in read mode
    with open("notes.txt","r") as file:
        content = file.read()
        if content:                           #if content exist(non empty)
            print("\nYour Notes:\n" + content)#Concating my String
        else:
            print("Notes Not Found")



def newnote():                   #open in append mode
    new_note=input("Enter New NOTE : ")
    with open("notes.txt","a") as file:
        file.write(new_note +"\n")#writes each note in new line
        print("Note Saved!")


    
# add timestamps,delete notes,categorise them .
