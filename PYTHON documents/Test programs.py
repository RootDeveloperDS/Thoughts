"""Concatenation"""

a="hello"
b="world"
str=a+b
print(str)

print(len(str))
#indexing
print(str[5])
#str[0] = ‘B’ not allowed

#slicing
print(str[2:7])        #llowo
print(str[:-6])        #hell

    #String Functions
str = "i am a coder."
print("\n",str)
print("str.endswith(","er.,"")" "\t",str.endswith("er.") ) #returns true if string ends with substr 
print("str.capitalize( )\t",str.capitalize( ) ) #capitalizes 1st char 
print("str.replace( \"code\", \"programme\" )\t",str.replace( "code", "programme" ))  #replaces all occurrences of old with new string
print("str.find( \"prog\" )\t",str.find( "prog" ))  #returns 1st index of 1st occurrence
print("str.count(\"am\")\t",str.count("am") ) #counts the occurrence of substr in strin



#WAP to input user’s first name & print its length.
name=input("enter name")
print("length:",len(name))
# WAP to find the occurrence of ‘e’ in a String.
print("no. of e:",name.count("e"))



#Conditional statements
#WAP to check if a number entered by the user is odd or even
no=int(input("enter no."))
if no%2 ==0:
    print("even")
else:
    print("odd")

