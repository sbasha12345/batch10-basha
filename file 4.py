
#  2nd answer
# num = 8
# factorial = 1
# for i in range(1, num + 1):
#    factorial *= i
# print("Factorial of", num, "is:", factorial)

# 3rd answer
# sum_even = 0
# sum_odd = 0
# for num in range(12, 38):
#    if num % 2 == 0:
#        sum_even += num
#    else:
#        sum_odd += num
# print("Sum of even numbers:", sum_even)
# print("Sum of odd numbers:", sum_odd)



# 4th answer
# n1 = 123
# total = 0
# while n1 > 0:
#    digit = n1 % 10
#    total += digit
#    n1 //= 10
# print("Sum of digits of the number:", total)

# 5th answer
# n1 = 234
# reverse = 0
# while n1 > 0:
#    digit = n1 % 10
#    reverse = reverse * 10 + digit
#    n1 //= 10
# print("Reverse of the given number:", reverse


# ---> while loop
# ----> break using while loop

# eg:1
# 1.)Iterate from 20 to 30 and break the loop in 27
#i = 20
#while i<31:
#    if i == 27:
#        break
#    print(i)
#    i+=1
   
# 2.)
#i = 20
#while i<31:
#    print(i)
    
#    if i == 27:
#        break
#    i+=1

# 3.)
#i = 20
#while i<31:
#    print(i)
#    if i == 27:
#        break
#    i+=1

#i = 20
#while i<31:
#     if i==27:
#        continue
#        print(i)
#        i=i+1

# Eg:5
# while to iterate from 12 to 22
# find the sum of all numbers

i = 12
while i<22+1:
     print(i)
     i+=1

i = 12
while i<23:
    sum=0
    sum=sum+1
    print(sum)
    i+=1


i=12
add=0
while i<=23:
    add+=i
    i+=1
    if i==23:
        print("sum of number is:",add)

# Eg:6
# Find the average of value from 20 to 25

#i=20
#sum=0
#while i<=25:
#    sum=sum+i
#    avg=sum/6
#    i+=1
#print(avg)

#i=20
#sum=0
#count=0
#while i<=30:
#    sum=sum+i
#    count+=1
#    i+=1
#    print(sum/count)

for row in range(1, 3+1):
    for col in range(1, 4+1):
        print(row, col)


# eg 22
# * * * * 
# * * * * 
# * * * * 
# * * * * 
for row in range (4):
    for col in range(4):
        print("*")

for row in range(4):
    for col in range(4):
        print("*",end=" ")
    print()
for row in range(4):
    for col in range(4):
        print("*",end=" ")
    print()


# ! to print stars in right angled triangle

for row in range(0,8):
    for col in range (0, row):
        print("*", end=" ")
    print()

#Eg:3
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
 
rows = 6

for i in range(rows, 0, -1):
    for j in range(0, i):
        print("*", end=' ')
    print("\n")

#*****
#*   *
#*   *
#*   *
#*****

rows = 5
cols = 5

for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end='')
        else:
            print(" ", end='')
    print()
    
    
for row in range(5):
    for col in range(5):
        if col==0 or col==5-1 or row ==0 or row ==5-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


#      *
#    * * *
#   * * * *
#  * * * * *

rows = 9

for i in range(rows):
    print(" " * (rows - i - 1), end='')  
    print("*" * (2 * i + 1), end='')    
    print(" " * (rows - i - 1))


# *
# * *
# *   *
# *     *
# *       *
# * * * * * *

for row in range(6):
    for col in range(6):
            if(col==0 or (row==0 and col==0) or (row==1 and col==1))or (row==2 and col==2) or (row==3 and col==3) or (row==4 and col==4) or (row==5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()

# ? ---> List

# 1.) if the collection of elements are surrounded by Square brackets, it is considered to be list.
# ! ---> Eg:
 l1 = [4, 7, 9, 9.89, "hello", 7+9j, [8, 9, 0]]


# Characteristics of list
# 1.) List have to be surrounded []
# 2.) It is mutable (the elements in the list are changable)
# 3.) Every elements inside list is indexed
# 4.) The elements inside list will be ordered format
# 5.) It can hold duplicate values
# 6.) Its heterogenous

# To access the elements in list
 lst1 = [1, 4, 1, 7, 89.7, 7.5, "p", "i"]
# print (l1)

# --> Indexing
# In the collection datatypes like list, tuple, string, the elements will be alloted
# with predefined unique value called index value

# We have 2 types of indexing
# Positive indexing --> starts with @ from left hand side
# Negative indexing --> starts with -1 from right hand side

# ? --> Positive indexing
 print(1st1[0])
#print(1st1[4])
 print(1st1[20]) --> error     

# ----> Negative indexing
#lst1 = [1, 4, 1, 7, 89.7, 75, "p", "i"]
#print(lst1[-1])
#print(lst1[-5])

# ? ----> slicing
lst1 = [1, 4, 1, 7,89.7,7.5 "p", "i"]
# lst1[start_index:end_index:step]

# print(lst1[0:4])
print(lst1[6:8])
print(lst1[3:6])
print(lst1[:5])
print(lst1[3:])
print(lst1[:])

print(lst1[0:7:1]) # lst1[0:7] --> both are same
#print(lst1[0:7:2])

# trail = int(input())


lst1 = [1, 4, 1, 7, 89.7, 7.5,"p", "i"]
print(lst1[-4:-1])
print(lst1[-1:-4]) --> []
print(lst1[-7:-1:2])

#! To insert ot add element inside list

# append()-> used to add elelement at last position of list
# 11 [9, 8, 0, 6]
# 11.append("car")
#print(11)
    
s1 = "hello world to all"
