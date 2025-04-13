import random
#WAP to check if a number entered by the user is odd or even
def one():
    while True:
        n=int(input("enter no. to check : "))
        oddeven(n)
        ans =input("do you wan to check again(yes/no). Type 0 to exit").strip()#stirip() to remove spaces
        if ans == "0":
            print("exiting...")
            break

def oddeven(no):
    if no%2 ==0:
        print("even")
    else:
        print("odd")


def randomno():
    max_a=int(input("Enter the highest number "))
    min_b=int(input("Enter the lowest number "))
    print("generated no. is : ",random.randint(min_b,max_a))
    in1 = input("type \'r\' to run same again,or anything else to stop  ")
    if in1 == 'r':
        randomno()
    else:
        print("STOPED...\n")
        masterfunct()
           
    
def factorial():
    num_f=int(input("Enter no. to find its factorial :  "))
    factoriall=1
    if num_f<0:
        print("Factorial dont exist")
    elif num_f==0:
        print("Factorial of 0 is 1")
    else:
        for i in range (1,num_f+1):
            factoriall*=i
        print("Factorial of ",num_f,"is : ",factoriall)

    print("\n")
    masterfunct()


def table():
    num=int(input("Enter no. to find its Table :  "))
    i=1
    while i<=10:
        print(num,"*",i,"=",num*i)
        i+=1
    print("\n")
    masterfunct()










def masterfunct():
    userin=int(input("Enter 1 TO check Odd Even no.\nEnter 2 To find the random no.\nEnter 3 To find the factorial of a no.\nEnter 4 To find the table of no. \nEnter 5 To find the \nEnter 0 To EXIT\n"))
    if userin == 1:
         one()
    elif userin ==2 :
        randomno()
    elif userin ==3 :
        factorial()
    elif userin ==4 :
        table()
    elif userin ==5 :
        g()
    else:
         print("Exiting.......")



masterfunct()   #here is start of program
