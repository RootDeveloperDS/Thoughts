#Declaring Dictionary
student={"name":"Devansh","age":20,"course":"B.Tech CSE","college":"GGITS"}
print(student)

#Acessing values
print(student["name"])
print(student["age"])

                   #"""if not available,To avoid ERROR"""
                    
print(student.get("agee"))                              #none
print(student.get("agee","Not Available"))              #Not Available

#Modifying/Updating/ADDING
student["age"]=18
student["city"]="Jabalpur"
print(student,"\n")

#REMOVING
"""
pop(key)                    Removes Specific Key
del dictionary[key]         Delete a key
clear()                     Removes ALL elements
        """
student.pop("age")
del student["city"]
print(student,"\n")

#LOOPING
for key in student:
    print(key)              #Show only Keys
for values in student.values():
    print(values)           #show only values
for key,value in student.items():
    print(f"{key}:{values}")#Shows both Key Value


print(student.values())
print(student.items())


#METHODS
"""
.keys()         #return all keys
.values()       #return all values
.items()        #return key-value pairs
update(dict2)   #merges another dictionary
copy()          #creates dict copy
            """

#######PRACTICE PROBLEM###############PRACTICE PROBLEM###############PRACTICE PROBLEM###############PRACTICE PROBLEM###############PRACTICE PROBLEM###############PRACTICE PROBLEM########
Book={"Title":"Power","Author":"Robert","Year":2016,"Price":1000}

Book["Price"]=1500

Book.pop("Year")

for key,value in Book.items():
    print (f"{key},{value}")



