def rem_duplicate():
    userin=input("Enter Seperated by spaces")#takes input
    numlist=list(map(int,userin.split()))   #convert inputs to a list of numbers
    unique_num= set(numlist)                #convert it o set

    print("Unique no.: ",list(unique_num))  #convert to list again







rem_duplicate()
