#sets {}    Unordered,Unique(no duplicate values)

# 1. creating SET
 #EMPTY SET
emptyset=set()          # {} will create dict so use set()
 #filled SET
myset={1,2,3,4,5,6}
print(myset)

# 2. Adding & Removing Elements
myset={1,2,3}
#Adding
myset.add(4)
print(myset)
#Removing
myset.remove(4)
print(myset)
#Removing Without Giving Error
myset.discard(10)       #no Error if 10 not found
print(myset)


# 3. SETs OPERATIONs - Union,Intersection,difference
A={1,2,3,4}
B={3,4,5,6}
print(A | B)    #Union          {1,2,3,4,5,6}
print(A & B)    #intersection   {3,4}
print(A - B)    #Difference     {1,2}
print(B - A)    #Difference     {5,6}
print(A ^ B)    #Symmetric difference{1,2,5,6}          removes common elements

# 4. Checking membership
myset ={1,2,3,4}
print(3 in myset)   #True
print(10 in myset)  #False

# 5. Converting LIST to SET (Removing duplicates)
mylist=[1,2,2,3,4,5,4,6]
myset=set(mylist)
print(myset) #{1,2,3,4,5,6}



####### PRACTICE PROJECT ############### PRACTICE PROJECT ############### PRACTICE PROJECT ############### PRACTICE PROJECT ############### PRACTICE PROJECT ############### PRACTICE PROJECT ########
"""Remove duplicates from list"""
