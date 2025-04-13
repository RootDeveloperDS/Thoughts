def divide():
    try:
        num1=int(input("Enter first no."))
        num2=int(input("Enter second no."))
        print(num1/num2)
    except ZeroDivisionError:
        print("cant divide by zero")
    except ValueError:
        print("Invalid input")




while True:
    print("\n1. Divide")
    print("2. Exit")
    choice=int(input("Enter Choice : "))
    
    if choice == 1:
          divide()
    elif choice == 2:
        print("Exiting...")
        break
    else:
        print("Invalid choice! ")

        
