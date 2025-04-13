
def viewnote():                   #open noted in read mode
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


    
#add timestamps,delete notes,categorise them

def search_notes():
    keyword = input("Enter keyword to search: ").lower()
    with open("notes.json", "r") as file:
        notes = file.readlines()
    
    found = [note for note in notes if keyword in note.lower()]
    
    if found:
        print("\nMatching Notes:")
        for note in found:
            print(note.strip())
    else:
        print("No matching notes found.")

#📌 Now users can find notes using a keyword!


#🔐 2️⃣ Password-Protected Notes
#Ask for a password before viewing or modifying notes.

PASSWORD = "12345"  # Set your password

def authenticate():
    entered_password = input("Enter password: ")
    return entered_password == PASSWORD

def view_notes():
    if not authenticate():
        print("Wrong password! Access denied.")
        return
    with open("notes.txt", "r") as file:
        print("\nYour Notes:\n" + file.read())

#📌 Now only authorized users can access notes!
        
#📂 3️⃣ Using JSON for Notes

#Store notes in a structured format (title, timestamp, category).


import json
from datetime import datetime

def save_note():
    note = input("Enter your note: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)  # Load existing notes
    except FileNotFoundError:
        notes = []  # Start fresh if file doesn't exist
    
    notes.append({"note": note, "timestamp": timestamp})  # Append new note
    
    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=4)  # Save notes in JSON format
    
    print("NOTE saved!")

def view_notes():
    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)
            for note in notes:
                print(f"[{note['timestamp']}] {note['note']}")
    except FileNotFoundError:
        print("No notes found!")

"""
📌 Now notes are stored in notes.json like this:

[
    {"note": "Buy groceries", "timestamp": "2025-03-06 14:30:45"},
    {"note": "Complete project", "timestamp": "2025-03-06 16:00:12"}
]
"""




############### TO DELETE NOTE ###############
def delete_note():
    with open("notes.json", "r") as file:
        notes = file.readlines()

    if not notes:
        print("No notes to delete!")
        return

    for i, note in enumerate(notes, 1):  # Show numbered list
        print(f"{i}. {note.strip()}")

    num = int(input("Enter note number to delete: ")) - 1

    if 0 <= num < len(notes):
        del notes[num]  # Remove the selected note
        with open("notes.json", "w") as file:
            file.writelines(notes)  # Rewrite remaining notes
        print("Note deleted!")
    else:
        print("Invalid note number!")







while True:
    print("\n1. Write a Note")               #Displaying MENU
    print("2. View Notes")                   #Infinite loop
    print("3. Search Notes")
    print("4. Delete Notes")
    print("5. Password-Protected Notes")
    print("6. Exit.")

    choice=input("Enter Your Choice : ")     #Choice Handling
    if choice == '1':
        #newnote()
        save_note()
        
    elif choice =='2':
        #viewnote()
        view_notes()
        
    elif choice =='3':
        search_notes()
        
    elif choice =='4':
        delete_note()
        
    elif choice =='5':
        authenticate()
        view_notes()
        
    elif choice =='6':
        print("Exiting...")
        break
    
    else:
        print("Invalid choice! Try Again.")

