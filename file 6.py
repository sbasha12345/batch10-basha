'''
s1 = "hello world"
fst = s1[0].upper()
lst = s1[-1].upper()

print(fst+s1[1:len(s1)-1]+lst)

print(s1.replace('h', 'H'))
print(s1.replace('d', "D"))

n = 128
i = 0
while n!=0:
    rem = n%10
    check= temp % rem
    if check!-0:
        f1 = 1
    n = n//10
   
 if f1==0:
         print("yes")
    else:
         print("no")

l1 = [8, 9, 0, 7]
l2 = [7, 6, 5, 4]

#print(l1[0]+l2[0], l1[1]+l2[1])
l3 = []
for val in range(len(l1)):
    ans = l1[val]+l2[val]
    l3.append(ans)
print(l3)'''

'''
# ! ----> set

# ? charactristics of set
# 1.) set can be treated using {}
# 2.) The element inside set are not indexed
# 3.) Does not allow duplicate values
# 4.) it unordered
# 5.) heterogenous
# 6.) mutable or changable

# Eg:1
s1 = {9, 89, 7.76, 8+7j, (8, 7, 5), "truck", 'e'}
print(s1)

# * Eg:2
#s2 = {5, 8, 98, [9, 0]}
#print(s2) ----> error


# Eg: 4
# min(), max(), len()

# * Eg:
# ? to add element inside set

s1 = {8, 78, 67, 'u'}
#add
#s1.add(43)
print(s1)

# ? to delete element inside set
s1 = {8, 78, 67,'u'}

#pop() # to delete one element randomy
# s1.pop()
# print(s1)

# removal()
# s1.remove(78)
# print(s1)

# discard()
# s1.discard(8967)
# print(s1)

## clear()
l1 = {}
print(type(l1)) ---- datatype is dict

s1 = set() # to creat empty set
print(type(s1))


# clear()

l1 = {}
print(type(l1)) 


s1 = set() # --> to create empty set
print(type(s1))

s1 = {8,9,0}
s1.clear()
print(s1)

s1 = {8,9,0}
del s1
print(s1)


# * Join the sets
#s1 = {9, 0, 8}
#s2 = {9.90, "card", 't', 56}
# union() ---> to combine 2 sets
#s3 = s1.union(s2)
#print(s3)


# intersection()  ---> get common elements inside set
#s1 = { 4, 5, 6}
#s2 = {5, 6, 7, 8}
#print(s1.intersection(s2))

# * difference()
s1 = { 4, 5, 6}
s2 = {5, 6, 7, 8}
print(s1.difference(s2))
print(s1.difference(s1))
print(s1.symmetric_difference(s2))

# isdisjoit(), issubjet(), issuperset()
# s1 = {8, 9, 0}
# s2 = {6, 7, 5, 8, 9, 0}

#print(s1.issubset(s2))
#print(s2.issuperset(s1))


# ! ---> problem:1

s1 = {1,2,3,4,5}
s2 = {3,2,7,8,9}

for val in s1:
    if val in s2:
        str1 = "Its joint set"
print(str1)


# ! ----> dictionary
# eg:1
d1 = {1:100, 'a':200, 4.5:"hello"}
mark_stud1 = {"English": 79, "maths"20, "physics":60}

# print(d1)
# print(len(d1))

mech_name =["name1", "name2", "name3"]
mech_age = [23, 22, 24]
mech_mark = [89, 78, 60]
mech_email = ["name2@gmail.com", "name3@gmail.com"]


mech = {
    "student1":{
        "name":"name1"
        "age":24,
        "mark":89,
  },
   "student2":{
        "name":"name2"
        "age":24,
        "mark":89,

  },
   "student3":{
        "name":"name3"
        "age":24,
        "mark":89,



# ? char of dictionary
# 1.) Have to be surrounded by{}
# 2.) It have to be in the form of key,value pair
# 3.) It is mutable
# 4.) Duplicate keys are not allowed,Duplicate values are allowed
# 5.) It is unidexed,It is ordered
# 6.) Key does nat allow mutable datatypes Values allow mutable datatypes   


d1 = {1:100, 2:200, 3:300, 4:400}
# * To access element in dictionary

# print(d1)
# or
# To access the values, haveto use key
# print(d1[1]) # o/p --> 100

# ? some common functions
# len(), min(), max()
print(min(d1))
print(max(d1))

# ? To find min, max based on values
print(min(d1.values()))
print(max(d1.values()))

# Dictionary based functions
# To add element(key and value pair) in dict

d1 = {1:100, 2:200, 3:300, 4:400}
d1[5]=500
print(d1)

# To replace a value in dictionary
d1={1:100, 2:200, 3:300, 4:400}
d1[2]= "mango"
print(d1)        

#? to delete a value in dictionary
# d1={1:100,2:200,3:300,4:400}
d1.popitem()
print(d1)

#delete element from dictionary

#d1 = {1:100, 2:200, 3:300, 4:400}
#popitem()
#d1.popitem()
#print(d1)


#pop
#d1.pop(2) #2 is the key in dictionary
#print(d1)

# clear(),del

# join 2 ditionary
#d1 = {1:100, 2:200, 3:300, 4:400}
#d2 = {"a":"apple","b":"ball","c":"cat"}
#d1.update(d2)
#print(d1)

# get()
d1 = {1:100, 2:200, 3:300, 4:400}

# get() ---> used to get the value from a ley
#print(d1[3])
#print(d1.get(90))


#to print the all the keys()
#print(d1.keys())
#print(type(d1.keys()))

# to print all the values
print(d1.values)

# * Iterating dictionary
for val in d1: # to iterate keys alone
    print(val)

for val in d1.values(): #  # to iterate values alone
    print(val)

# to get both key and values
for key, val in d1.items():
    print(key, val)

# ! problem:1

# n = input()
# 1.) swap elemwnts in string list
# The original list is :["Ggf", "best", "for", "geeks"]
# List after performing character swaps:]"efg", "is", "bBgst", "for", "eGGks"]

test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']
 
# printing original lists
print("The original list is : " + str(test_list))
 
# Swap elements in String list
# using replace() + list comprehension
res = [sub.replace('G', '-').replace('e', 'G').replace('-', 'e') for sub in test_list]
 
# printing result 
print ("List after performing character swaps : " + str(res))
Output : 
The original list is : ['Gfg', 'is', 'best', 'for', 'Geeks']
List after performing character swaps : ['efg', 'is', 'bGst]'''
                                         

'''
# ! problem:1

n = int(input("Enter the value: " ))
integer=[]
float_value =[]
string=[]

for val in range(n):
    value = eval(input("enter the values: "))
    if type(val)==int:
        integer.append(val)
    elif type(val) == float:
         float_value.append(val)
    elif type(val)== str:
        string.append(val)
    else:
        print("p1s provide data in int, float, string")      
print(integer)        
print(float_value)        
print(string)
'''

# ! problem:2

return a set elements present in set A or B, but not both
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}



set3 = set()
for val in set1:
    if val not in set2:
        set3.add(val)
for val in set2:
    if val not in set1:
        set3.add(val)

print(set3)

#! ---> problem 3
l1=[1,2,3,4] # key
l2=["a","b","c","d"]  # value
l3=(l1[0],l2[0]or l1[1],l2[1] or l1[2],l2[2]or l1[3],l2[3])
print(l3)


# 1.) Swap elements in String list
# The original list is : ['Gfg', 'is', 'best', 'for', 'Geeks']
# List after performing character swaps : ['efg', 'is', 'bGst', 'for', 'eGGks']

                                         
# ----> Assesment
# 1.) dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# Merge two python dictionary
# o/p --> {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# 2.)Python Program to determine if 
# the given Sets Are Disjoint 
# or Not without Using Inbuilt-in Functions

# set1 = {'Python', 'Java', 'Data Science'}
# set2 = {'ML', 'AI', 'R Language', 'Python'}
# set3 = {'Data Analytics', 'Robotics', 'Deep Learning'}

# 3.)list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]

# O/P --> ['My', 'name', 'is', 'Kelly']
