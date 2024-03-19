
    
# ! Eg:3
def profile(name, age, place):
    txt =" my name is {}. Iam {} years old. Iam from {}."
    print(txt.format(name, age,place))
profile("basha", 23, "cbe")


# ! Eg:4
# ? Function with return statement

# ! return
# 1.) A variable declared inside the function can be accessed outside using return
# 2.) return does not prrint anything
# 3.) we cannot write any code below return statement

def f1():
    z = 8
f1()
print(z) # error ---> cannot use outside the function


def f1(a, b):
    c = a*b
    return c
print(f1(6, 8))
obj = f1(6, 8)
obj1 = f1(4, 6)


def gracemark(object):
    print(object+4)
  gracemark(obj)
  gracemark(obj1)




# 123
def palindrome(n):
    string = str(n)
    rev = str(n)[::-1]
    if string==rev:
         print(n, "palindrome")
    else:
         print("Not palindrome")    
a = int(input("Enter the value: "))
palindrome(a)

# ? Based on the declaration on parameter and args
# ? fonctions are divided into 5 catagories

# positional args
# keyword args
# default args
# variable length args
# keyword variable length args


# * positional args
# ? The position of parameter have to be same as position or arguments
# Eg:1
def profile(name, phone, mark):
    txt = "My name is {}. My phone number is {}. I got {} mark."
    print(txt.format(name, phone, mark))

profile( "basha", 8374083257, 98) # unexpected output
          
# keyword args
# ! Eg:1
# ? To overcome the disadvantage of position args, we use keyword args
          
def profile(name, phone, mark):
    txt = "My name is {}. My phone number is {}. I got {} mark."
    print(txt.format(name, phone, mark))

profile(name = "basha",phone = 8374083257,mark = 98)

# todo ----> Exception of keyword args function
def profile(name, phone, mark):
    txt = "My name is {}. My phone number is {}. I got {} mark."
    print(txt.format(name, phone, mark))

# profile(name = "basha", 8374083257,mark = 98) # error -> positional args follow keyword args
# profile(8374083257, name="basha", mark =98)# error --> name has multiple values
profile("basha", mark=98, phone=8374083257)


# * Default args
# the method of assiging the argument to the parameter while declaring
# the function

# ! Eg:1
def profile(name, phone,place):
    txt = "My name is {}. My phone number is {]. I am from {}."
    print(txt.format(name, phone, place))

profile("basha", 8374083257)    

# ! Eg:2
def profile(name, phone,place):
    txt = "My name is {}. My phone number is {]. I am from {}."
    print(txt.format(name, phone, place))


Problem Statement: Given a string S(input consisting) of ‘*’ and ‘#’. 
The length of the string is variable. The task is to find the minimum number of ‘*’ 
or ‘#’ to make it a valid string. The string is considered valid if the number of ‘*’ 
and ‘#’ are equal. The ‘*’ and ‘#’ can be at any position in the string.
Note : The output will be a positive or negative integer based on number of ‘*’ 
and ‘#’ in the input string.

(*>#): positive integer
(#>*): negative integer
(#=*): 0
    
###***   -> Value of S
Output :

0   → number of * and # are equal
Exception
profile(name, phone, place="kadapa"):
    if place |="kadapa" or place |= "kadapa" or place=="kadapa":
    txt = "My name is {}. My phone number Is {}. I am from {}."
    print(txt.format(name,phone,place))
else:
    print("you are not eligible to signup")
profile("basha",8374083257)

def profile(name, place="kadapa",phone): # error --> coz default args should not follow
                                         # positional param
    if place |="kadapa" or place |= "kadapa" or place=="kadapa":
    txt = "My name is {}. My phone number Is {}. I am from {}."
    print(txt.format(name,phone,place))
else:
    print("you are not eligible to signup")
profile("basha",8374083257)


# * variable length(*name):
# ! Eg:1 --->
# To pass more then 1 arg to a parameter means we use variable length args
# to convert normal parameter to variable length param,
# add 8 to ther prefix of parameter

name = "bas", "name1", "name2"
def profile(*name):
    print("My name is",name)
profile("bas" 'name2','name3')


name = "bas", "name1", "name2"
for val in name:
    print("My name is",val)

    
# ! Eg:2 --->

def profile (*name, age):
    for val in name:
        print("My name is ",val,"my age is ",age)
profile("pramod", 'name2', 'name3', 26) # error --> age has no args


        
def profile (age,*name):
    for val in name:
        print("My name is ",val,"my age is ",age)
profile(26, "pramod", 'name2', 'name3')


# * keyword variable length args
# ! Eg:1
def price(price_list):
    print(price_list)

print(shirt=1000, iphone=80000)

#n = 5
#{1:1, 2:4, 3:9, 4:16, 5:25}



d1 = {"a":100, "b":200, "c":300}
d1 = dict(a=100, b=200, c=300)
print(d1)

# n = int(input("Enter the number: "))

d1 = {}
for val in range(1, n+1):
    d1[val] = val**2
print(d1)
# dictl(5)

# ! ----------> object oriented programming
# the paradigms of objects oriented programming are

# class
# objects
#inheritance
#polymorphism
#abstraction
# encapsulation

# ! class is a blue print of an object
# l1 = [1,2,3,4,5,6]

# Eg:2
class c1:
    name1 = "basha"
    print(name1)

# ? Eg:3
# create of a method
# when the function is created with a class is called as method

# ! Mehod without parameter
class person:
    def display(person): # it is a method 
        print("Hello welcome to classes")
p = person()
p.display()


# ? Eg:4
# ! Method with parameter
class person:
      def display(person, name, age):
          print(name, age)

  p = person()
  p.display("sidhu",28)


# ? Eg:5
class person1:
    fname = "basha" # attribute or static variable
    name = "T"
    def display():
        print(name3)

p = person1()
p.first_name()
p.full_name()

# ? Eg:6
# constructions --> __init__()
# This is a special method which has the ability to execute to itself without
# calling it manullay through the process of instantiation

class profile:
    def__init__(self): # costructor method
        print("hey")
p = profile() # execution of constructor through this process

#1.) Write a Python script to generate and print a dictionary that #contains a number (between 1 and n) in the form (x, x*x). Sample Dictionary (n=5): # Expected Output (1:1, 2:4, 3:9, 4: 16, 5:25)
#2.) Find the uncommon words from 2 strings
##s1 "Hello how are you"
#52 "Hello how is"
#3.) Wrire a code print the 8th fihanochi number
        
