#FOR loop

fruits=["apple","banana","cherry"]
for fruit in fruits:
    print(fruit)


#using range
for i in range(1,6):     #1,2,3,4,5
    print(i)


#WHILE loop
count=1
while count<=500:
    if count == 1:     #stops at 249
        break            #using BREAK
    print(count)
    count+=1

for num in range(1,10):
    if num ==8 or num== 9:
        continue
    print("\n",num)
