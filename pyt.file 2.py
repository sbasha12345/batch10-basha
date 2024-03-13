
a, b=c=7, 8
print(a)
print(b)
print(c)

a=b ,c=4, 2
print(a, b, c)

#----> swapping of variables
a=7
b=5
print(a,b)
# Eg:1
print(a,b)
temp=a #temp=7
a=b    #a=5
b=temp #b=7

# # a=5, b=7
# print(a,b)

# Eg:2
# a=a+b #a=12
# b=a-b #b=12-7=5
# a=a-b #$a=12-5=7

#print(a, b)

# a, b=b,a # only in python
# print(a, b)

a=a*b #a=35
b=a/b #b=35/7 = 5.0
a=a/b #a=35/5 = 7.0
print(int(a),int(b))

id()---> used to find the memory address of the variable
a = 7
print(id(a))
print(id(b))

# ----> keywords
# keywords are reserved words which provides special
# compiler or interpeter

import keywords
print(len(keywords.kwlist)
print(type(keyword.kwlist)

# to check if the string is keyword or not
print(keyword.isksyword("og")) # false

if = 8
print(if)#error coz if is a keyword

# !---> literals
# literal is the constant value assigned to a variable
# A variable is considers to be constant when it is defines
# in caps

# a=78 # a is variable
# A=78 # A is constant
      
#hash() --> it creates a hash value for constant datatypes and
# provides error for non constant datatypes      
n1 = 89+7j
print(hash(n1))      
      
f1 = [7,8,9]
print(hash(f1)) # error -->list is non constant or mutable datatype
# a = 9
# b = 9
# b= 90
# print(id)(a))
# print(id)(b))
      
# ! ----> Operaters
# ? operaters are symbols which is to perform various operations
# ? between 2 or more operands
# Arithmatic
# Assignment
# Logical
# Relational or comparison
# Bitwise
# Identity
# Membership

# todo ---> Arthimatic --> +,-,*,/,%,//,**
# Eg:1
# a = 8
# b = 6
# c = 9
# print(a+b+c)


input () --> used to get the runtime input
n1 = input(" ENTER THE VALUE:")
print (type(n1))
      
# a = 4
# b = 2
# Print(a/b) # is used to get the quoient value
# print(a%b) # is used to get the remainder value      

# ! // --> floor devision
# a = 765433
# b = 19
# print(a//b) # -> the output will be integer & the output will be
# based on floor value

#!  ** --> used for power of a number
print(2**4) # --> 16

# ! Assignment --> +-=, -=, /=, //=, **=,&=,|=
# a= 8
# a+=2
print(a)

# a=30
# a-=5
print(a)

# ! comparison --> ==, >, <, !=, <=,>=
# a = 8
# b = 7

print(a>b) # True

# ! Bitwise operator --> &,|,^,~,<<,>>
# a = 7
# b = 4
print(a&b)

# 2^4 2^3 2^2 2^1 2^0
# 8   4   2   1
# 0   1   1   1   # -->7
# 0   1   0   0   # -->4 &
# -------------------      
# 0   1   0   0

# 256 128 64 32 16 8 4 12 1
#  0   0   0 0  0 0 0 1 0 0      
      
# ! Logical --> used to compare the expressions
# and , or , not
# a = 6
# print (a>3 and a>10)
# print (a>7 or a>30)
# print (not(a>8 and a<10))

# ! identify operator
# is, is not
a = 8
a = 8       
# print(a is b)
#print(a==b)

# a = [1, 2, 3,]
# b = [1, 2, 3,]
# print(a is not b)

# ! Membership operator
# in, not in
l1 = [7, 8, 9, 0, 6, 5]     
# num = 55
# print (num in l1)
# print (num not in l1)

# num = 678
# print(8 in num) # error

# ! conditional statement
# if , else ,elif

# Eg:1
#  --> C syntax      
# if (condition){
      statement;
      statement;
      statement;
#}
# python syntax
# if condition:
      statement
      statement
      statement
# statement

# eg:1
a = 6
# if a:
# print("hello")

# Eg:2
a = 6
if a>3:
      print("hey")
      print("yes")
else:
      print("no")

#Eg:3
#if 7>8:
     print("hello")
else:
     print("no")

#Eg:4
# a = 0
# a = None
# a = False

------------------------------------------
# a number is even or odd
 n = int(input("enter the number: "))
if n %2==0:
    print(n, "is even")
else:
     print(n, "is odd")
# name, age, nationality
#  18 above, Indian

#str ("name is basha")
#int ("age is above 18")
#str ("nationality is indian")

name = input("Enter the name: ")
age = int(input("enter the age:")
nationality=input("enter the nation:")

if age>=18 and nationality=="indian":
          print("eligible for vote")
else:
    print("not eligible")

       
      



