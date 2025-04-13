import random as ran
def rolldice():
    return ran.randint(1,6)




while True:
    inp=input("press enter to roll again..")
    if inp != '0':
        print("you rolled : ",rolldice())
