#1. Creating strings
str1='string'
str2="python"
str3="""Multiline
string"""

##2. Accessing ,slcing,indexing
test='python'
print(test[0])  #p
print(test[-1])
print(test[1:3])    #yt
print(test[::-1])   ##nohyp[REVERSE the string]

###3. Methods
s="  Hello Sir  "
s.upper()#  HELLO SIR   
s.lower()#  hello sir
s.strip()#hello sir(removes spaces)
s.replace("hello","Hi")#Hi sir
s.split()   #["Hi","sir"]           split into words

#~to chect if word is in sting

text="Python is fun"
print("Python" in text)#True
print("Java" not in text)#True

####4. String Formatting
 #~1 Using f-string (Best And modern)
name='devansh'
age=18
print(f"my name is {name} and age is {age}")

 #~2 Using  .format()
print("my name is {} of age {}".format(name,age))

#####5. Joining and Concatenation
words=["Python","is","fun"]
sentence=" ".join(words) #Python is fun
print(sentence)


####### PRACTICE PROJECT ############### PRACTICE PROJECT ############### PRACTICE PROJECT ############### PRACTICE PROJECT ############### PRACTICE PROJECT ############### PRACTICE PROJECT ########
"""project= word counter in sentence"""
