# ! Eg:3
# ? Take values of length and breadth of a
# ? from user and check if it is square or not

#length = int(input())
#breadth = int(input())
# if length==breadth:
#  print("its a square")
# else:
#    print("its not a square")

# ! Eg:4
# Python program to chechk whether the
# given integer is a multiple of both 5 and 7

# n=int(input("enter the number: "))
# if n%5==0 and n%7==0:
#    print("yes")
# else:
#    print("no")


# ! Eg:5
# write a program to accept the cost price of a bike and display the
# road tax to be paid
# according to the following criteria :

#       cost price (in Rs)                                Tax
#       >100000                                            15 % + discount 6%
#       >50000 and < = 100000                              10%
#       <50000                                             5%


#price = int(input("enter the price"))
#amount = 0
#if price >=100000:
#   discount = price*(6/100)
#   value = price-discount
#   amount=value*(15/100)
#   total = value+tax
#else:
#    tax = price*(5/100)
#    total = price+tax
# print("The onroad cost of bike is: ",total)


# !------> if elif else
# Eg:1
#a = 8
#b = 9
#c = 6

#if  a>b and a>c:
#    print("A is greater")
#elif b>a and b>c:
#    print("B is greater")
#elif c>a and c>b:
#    print("C is greater")



# A school has following rules for grading system
# a.below 25 - F    
# b.25 to 45 - E
# c.45 to 50 - D
# d.50 to 60 - C
# e.60 to 80 - B
# f.above 80 - A
# Ask user to enter the marks and print the corresponding grade

# mark = int(input("enter mark: "))
# if mark>=80 and mark<=100:
#    print("A")
# elif mark>=60 and mark<80:
#    print("B")
# elif mark>=50 and mark<60:
#    print("C")
# elif mark>=40 and mark<50:
#    print("D")
# else:
#    print("fail")


# ! Eg:6
# ? accept the age of 4 people and display the oldest one.

# ! --> short hand if else
# Eg:1
#a = 9
#b = 6
# if a>b:
#      print("A")
# else:
#       print("b")
#? --> using short hand if else
# * rules
# 1.) statement inside the if condition have to be present at first
# 2.) elif cannot be used in short hand if else
# 3.) always it have to end with else

# print ("A") if a>b else print("b")




# ! code to check the given char is vowel or consonent
# char = input("Enter the char:")

# if char=="a" or char=="e" or char=='i' or char =='o' or char =='u':
    #  print(is a vowel")
    #else:
    #  print("its consonent")

    # ? or

#    str1 ="aeiouAEIOU"
#    if char in str1:
#       print("vowel")
#  else:
#     print("consonnt")
        


# ! --> elif ladder using shorthand if else
# Eg:1
# ? find greatest among 3 variables using short hand if else
#a=8
#b-5
#c=9

# print("A is greater) if a>b and a>c else print("B is greater")
# if b>a and b>c else print("C is greater")


# ! ---------> looping

# looping can be implimented using
# for loop
# while loop

# ---> for loop
# ? for loop is used for iteration, if we know the number of times the loop have to run
# ? it is used to iterables eg(string, list, tuble, etc...)

# todo --> syntax for loop

# for syntax in c
# for (i=0;1<10;==){
#    print("hello");
# }
# ! for syntax in python
# for userdefined_variable in range(start,end,step): default step value is 1
#   statement
#   statement
#   statement

# ? Eg;1
# To print the value from 1 to 10 using for loop

#for i in range(0,10): #(n, n-1)
#    print(i)
#    print("hello")


# ? Eg:2
# to print the value from 1 to 10 using for loop

# for i in range(0,100):
#     print(i)


# ? Eg:2
# for val in range(1, 10, 2):
#     print(val) 

# for val in range(1, 10, 3):
#     print(val)

# ? Eg:3
# to decrement the value

# for val in range(10,0,-1):
#     print(val)


# for val in range(10,0,-2):
#      print(val)       

# for val in range(1, 10, 1):
#      print(val) 

# ? Eg:4
# ! print the output of 7th multiplication table 21 to 43
for val in range (1, 10+1):
    print('18','X', val,'=',val*18)

    # --> method:2
    ans="7 X {} = {}"
    # print (ans.format(val,val*7))

    # --> method:3
    print(f"7 X {val}={val*7}")


    # ? Eg:5
# break ---> used to terminate the loop

# for val in range(1, 10):
#     if val ==6:
#         break
#  print(val)

# ? Eg:6
for val in range(1, 100):
    print(val)
    if val ==98:
        break

    # eg:7
for val in range(1,10):
    print(val)
    if val ==6:
        break



# ? eg:8
for val in range(1,10):
    if val ==6:
        print(val)
        break
    

# ! continue
# Eg:1
for val in range(1, 1000):
    if val ==b:
        continue
print(val)

# ! practise problems
# ? print the even number between 20 to 40

for num in range(20, 41):
    if num % 2 == 0:
       print(num)


# ! continue
# Eg:1
for val in range(1, 1000):
    if val ==6:
        continue
print(val)

# ! Practise problems
# ? Print the even number between 20 to 40
for val in range(20,41):
    if val %2==0:
         print(val)

#!----------> while loop
# ? while is used when we do not know the number of times the loop wii have to run
# ? to literate the non literable elements while loop is used


# tool syntax


inltlalistation
while condition:
#     statement
#     incre or decre

#! Eg:1
# to iterate number from 1 to 10

# i = 0
# while i<11:
     print(i)


# for loop practice
# write a program to display sum of odd numbers and even_
# numbers that fall between
# 12 and 37 (including both numbers)


# ---> Assesment
# 1.) cats and mouse:Hacker rank
# 2.) Print the factorla of 8 using for loop
# 3.) Write a program to display sum of odd numbers and even 
# numbers that fall between
# 12 and 37(including both numbers)
# 4.) Write code to print the sum of number using while loop
# n1 = 123 --> 1+2+3 = 6
# 5.) Prine th reverse of given number --> n1= 234 o/p --> 432


