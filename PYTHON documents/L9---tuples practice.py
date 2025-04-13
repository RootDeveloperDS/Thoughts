#tuples,IMMUTABLE
mixed=(10,"hello",3.14,True)
print("\t",mixed)
#acessing elements
print("mixed[-3]\t",mixed[-3])
#slicing
print("mixed[1:-1:]\t",mixed[1:-1:])
print("mixed[::2]\t",mixed[::2])
#immutable
"""
mixed[1]="hi"
print("mixed[1]\t",mixed)
"""


#to modify tuple first conver it to the list by list() then to tuple()
#eg:-
mixed_list=list(mixed)
mixed_list[1]='hi'
mixed=tuple(mixed_list)
print ("\t",mixed)

#Concatenation joining
t1=(1,2,3)
t2=(4,5,6)
t3=t1+t2
print("t3   =  ",t3)
"""AND"""
print("t2*4 = ",t2*4)


#TUPLE  METHODS
"""
len(tuple)
.count(value)
.index(value)
"""

print(len(t3))       #6(length is 6 elements)
print(t3.count(5))   #1(occured only one time)
print(t3.index(5))   #4(5 have index of 4)


#using  LOOPS
t3=t1+t2
print("t3 =     ",t3)
#for loop
for t in t3:
    print(t)
#while loop
i=0
while i<len(t3):
    print(t3[i])
    i+=1
