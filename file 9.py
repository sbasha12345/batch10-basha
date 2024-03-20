
'''
# 1.) Write a Python script to generate and print a dictionary that
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary (n=5):
# Expected Output {1:1, 2:4, 3:9, 4: 16, 5:25}

# 2.) Find the uncommon words from 2 strings
# # s1 "Hello how are you"
# s2 = "Hello how is"
s1 = "Hello how are you"
s2 = "Hello how is"


s1 = s1.split(" ")
s2 = s2.split(" ")

for val in s1:
    if val not in s2:
       print(val)
       

for val in s2:
    if val not in s1:
       print(val)
               


# 3.) Wrire a code print the 8th fihanochi number
# 0, 1, 1, 2, 3, 5, 8

n1 = 0
n2 = 1
ans = 0+1 ==> 1

n1 = 1
n2 = 1
ans = 1+1 ==> 2

n1 = 1
n2 = 2
ans = 1+2 ==> 3

n1 = 2
n2 = 3
ans 2+3 ==> 5


# ! find the 8th fibonacci number

num = 8
n1 = 0
n2 =1

for val in range(num):
    ans = n1+n2
    n1 = n2
    n2 = ans
print(ans)

# ! constructors
# ? Eg:2
# * unparamentarised constructor
class profile:
    def__init__(self):
        print("hello world")

obj = Profile()
obj.__init__()


# ? Eg:3
# * parametarised costructor
class profile:
    def__init__(self, id, name, age):
        print(id, name, age)

obj = profil(1, "bash", 23)

# ? Eg:4
class c1:
    name = "bash"
    place= "cbe"

    def n1(self):
        print(self.name, self.place)

object = c1()
object.n1()'''

# ? Eg:5
class c1:
    def m1(self):
        name = "bash"
        age = 23
        return name, age
    def display(self):
        # ! print(name, age)
        # ! print(self.name, self.age)
        print(self.m1())
        
object = c1()
object.display()

# ! Eg:2

class c1:
    def __init__(self):
        print("Iam constructor from parent class")

class child1(c1):
    pass

obj = child1()

# ! Eg:3

class parent:
    name = "sai"

class child(parent):
    name = "name1"

    def display(self):
        print(self.name)

d = child()
d.display()

# ! Multilevel inheritance
# ? Eg:1
class voice:
    def sound(self):
        print("All the animals have their own voices")

class dog(voice):
    def dog_voice(self):
        print("bark")

class cat(voice):
    def cat_voice(self):
        print("meow")

class parrot(voice):
    def parrot_voice(self):
        print("speak")


all = parrot()
all.dog_voice()
all.cat_voice()
all.sound()
all.parrot_voice()


# ? Eg:2
class honda_city:
    def honda_city_engine_spece(self, cc, hp, torque, fuel_type, num_of_piston):
        print(cc, hp, torque, fuel_type, num_of_piston)
 
    def honda_city_body_spece(self, color, weight, height, length, vehical_type):
        print(self, color, weight, height, length, vehical_type)

class civic(amaze):
    def civic_engine_spece(self, cc, hp, torque, fuel_type, num_of_piston):
        print(cc, hp, torque, fuel_type, num_of_piston)
 
    def civic_body_spece(self, color, weight, height, length, vehical_type):
        print(self, color, weight, height, length, vehical_type)

class amaze(Honda_city):
     def amaze_engine_spece(self, cc, hp, torque, fuel_type, num_of_piston):
        print(cc, hp, torque, fuel_type, num_of_piston)
 
    def amaze_body_spece(self, color, weight, height, length, vehical_type):
        print(self, color, weight, height, length, vehical_type)

# class Honda(civic):
         pass

# honda = honda()
# honda.honda_city_engine_specs(1500, 230, 2979,"petrol",4)
# honda.civic_body_specs("white", 2000, 5.5, 8,"Hatchback")
        
# ! Multiple Inheritance
# ? It has multiple parent and 1 child

class while_petrol:
    print("used to Aeroplane")

class Organic_petrol:
    def function_o(self):
        print("used for Bike, cars")

class petrol(while_petrol, Organic_petrol, premium_petrol):
    def defanition(self):
print("Petrols types")

p=petrol()
p.defanition()
p.function()    
        
# ! Eg:2
class addition:
    def add(self, a, b):
        print(a+b)
class subract:
    def add (self, a, b):
            print(a-b)
class multiply:
    def mul(self, a, b):
        print(a*b)
class division(addition, subract, multiply):
    def div(self, a, b):
        print(a/b)
calc=division()
calc.add(3,4)
calc.mul(5,2)

# ? Heirarical inheritance
class catagory:
    def cal_name(self):
        print("vegetables")

class Tomato:
    def tomato_specs(self):
        color="black"
        taste = "neutral taste"
        self.display(color, taste)
        
class carrot(catagory):
    def carrot_specs(self):
        color="green"
        taste = "sweet"

c = carrot()
c.carrot_specs()
c.weight("30gms")

t = tomato()
t.tomato_specs()
t.weigth("30gms")


# Hydrid inheritance
# ? the combination of above 4 inheritance is called Hydrid inheritance

class c1:
    def m1(self):
        print("class1")

class c2(c1):
    def m2(self):
        print("class2")

class c3(c2):
    def m3(self):
        print("class 3")

class c4(c3):
    def m4(self):
        print("Iam m3 from c4")

class c5(c4):
    def m5(self):
        print("class 4")

class c6(c3, c5):
    def m6(self):
        print("class 4")

obj = c6()
obj.m3()


# ! --------------> Polymorphism
# ? poly - many, morph --> form
# A function which has the ability to perform more than 1 functionality
# then it is considered to be as plioymorphism


# * Polymorphism in builtin functions
# len() --> which is used to find the length of list, tuple, dict etc..
# index()
# max()
# min()
# count()
# pop() and more.....

# * ploymorphism in operators
# +
# print(8+8)
# print("k"+'l')
# print([1,2,3]+[5,6])

# *
#  print(6*7)
# l1 = {1,2,3,4,5,6}
# print(*l1)
# def f1(*args)
# l1 = [1,2,3,4]
# print(l1*10)


# ploymorphism in classes
# we can achieve polymorphism in 2 ways
# 1.) method overloading --> it is not possible in python
# 2.) method overriding

# 1.) Tasks
# ! Write the code for the belwo tasks using function
# ! )>d1 = {"shirt": 1000, "pant"; 1500, "Shoes"; "900", "handkey": 30}
# a.) Find the min ans max priced product
# b.) Find the product starts with 's' and 'S'

# 2.) Find then 67, is strong number or not

# 3.) 11 [1,2,3,4,5,6]
#   n=2> [5, 6, 1,2,3,4]
#n=3--> [4,5,6, 1,2,3]
