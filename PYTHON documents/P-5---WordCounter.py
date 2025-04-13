def wordcounter():
    string=input("Enter your sentence below : \n")
    
    wordslist=string.split()
    
    print(len(wordslist))
            #OR
    print(f"Total Words:{len(wordslist)}")






wordcounter()
