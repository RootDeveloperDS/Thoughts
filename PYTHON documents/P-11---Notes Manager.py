class NoteManager:
    def __init__(self,filename = "Notes.txt"):
        self.filename = filename

    def add_notes(self,note):
        with open(self.filename,"a") as file:
            file.write(note + "\n")
        print("Note Added! ")

    def view_notes(self):
        try:
            with open (self.filename,"r") as file:
                notes = file.readlines()
                if notes:
                    print("Your Notes:")
                    for i,note in enumerate(notes,1):
                        print(f"{i} - {note.strip()}")
                else:
                    print("No Notes found! ")
        except FileNotFoundError:
            print("Notes file not found!")


#Using notesmanager
note = NoteManager()

note.add_notes("first added note")
note.add_notes("second added note")

note.view_notes()


            
