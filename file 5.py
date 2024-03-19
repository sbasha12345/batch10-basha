# ! ------> common functions for list
#l1 = [6, 7, 8, 9, 0]
# print(len(l1))

#print(max(l1))
#print(min(l1))

#l1 = [6, 7, 9, "p","u"]
#print(max(l1)) # --> error coz its a combination of int and string
#print(min(l1)) # --> error coz its a combination of int and string

#l1 = [6, 7, 8, 9, 0, 8.89, -5, 0.78]
#print(min(l1)) # -5

#l1=[6,7,8,9,0,8.89,-5,0.78]
# index() ---> to get index value of specific element
#print(l1.index(9))

#l1=[6,7,8,9,0,8.89,-5,0.78]
# count()--->how many num of times an element is repeated
# print(l1.count(6))

# ! some functions which is specifically used for list

# To add element inside list
# ? insert () ---> to add element at specific index positions
#l1 = [6,6,6,7,8,9,0,8.89,-5,0.78]
#l1.insert(2, "cars")
#print(l1)


# ? to delete an element from list
#l1 = [6,6,6,7,8,9,0,8.89,-5,0.78]

# *pop(inde_valve) --> used to delete element at specific index
#l1 = [2,3,2,3,4,32,6.76,98.5,-94]
#l1.pop(5)
#print(l1)

# *remove(element) --> used to delete element directly
#l1 = [2,3,2,3,4,32,6.76,98.5,-94]
#l1.remove(6.76)
#print(l1)

# *clear() --> to complete delete all element in list

#l1 = [2,3,2,3,4,32,6.76,98.5,-94]
#l1.clear()
#print(l1)


# del -> to delete the list
#del l1 #or del(l1)
#print(l1)

# ? ----> join 2 lists

#l1 = [9, 0, 8]
#l2 = ["p", "o", "t",34]
# * print(l1+l2)

# ! or

# * extend()  ---> to combine 2 lists
# l1.extend(l2)
#print(l1)

# ? ------> copy()

# l1 = [6, 7, 8,9, 3]
# l2 = l1.copy()
# print(l2)
# print(l1)


# ! diff between shallow copy and deep copy
# shallow copy
import copy
l1 = [8,9,0,[5,6],[3, 2, 1]]
l2 = copy.copy(l1)
l1.append(890)
print(l1)
print(l2)

# deep copy
import copy
l1 = [8, 9, 0,[5,6],[3, 2, 1]]
l2 = copy.copy(l1)
l1.append(890)
print(l1)

# deep copy ---> used to copy the list with nested list 
import copy
l1 = [8,9,0,[5,6],[3, 2, 1]]
#print(l1[-1][l1]) #---> to index nested list

l2 = copy.copy(l1)
l1[-1].append("cars")
print(l1)
print(l2)

# M:-2 --> descending order

l1 = [9,7,2,3,5,23,63,32]
l1.sort(reverse=True)
print(l1)

# ? sort ---> arrange elements in list in ascending or descending order
l1 = [9, 7, 45, 0, -6, 5, 12]
l1.sort() # to arrange in ascending order
print(l1)

l1.sort(reverse=True) # to sort in descending order
print(l1)


l1 = ['z', 'i', 'o', 'p', 9]
l1.sort()
print(l1)# --> error



# ? list constuctor
# * list() ---> to conver other collection datatype to list
l3 = ((8, 9, 0))
print(list(13))

l4 = (8,9)
print(list(l4))

# ! ----> nestsd list

l1 = [8, 9,[0, 8, 7],["p","o","y"],[8, 't']]
# print(l1[-2][1]) # --->o


print(l1[1:4])
print(l1[1:-1])


# ? to delete "t" from l1
# L1[-1].REMOVE('t')
#print(l1)

# ? combine these ["p", "o", 'y'],[8, 't'] lists in l1 to ["p", "o", 'y', 8, 't']
l1[-2].extend(l1[-1])
l1.pop(-1)
print(l1)

# ! ------> Tuple
# *char of tuple

# 1.) tuple have to be sourrounded by ()
# 2.) the elements inside tuple are not changable
# 3.) the elements inside tuple are indxed
# 4.) the element will excute in order
# 5.) It is heterogenous
# 6.) It allow duplicate element
#eg:1
t1 = (8, 8, 9, 6, 5.78, [9, 0], "hey" , 9+6j)
print(t1)
print(type(t1))

# ? indexing, slicing are all same as list
print("hello")

l1 = [8]
print(type(l1)) #int

l1 = (8,)
#print(type(l1)) #tuple

t1 = 8,9
print(type(t1)) # tuple

t2 = 8,
print(type(t2)) # tuple

# len(), min(), inex(), count()-----> al same as list
# cannot delete any element from tuple

# * join 2 tuples
t1 = (8, 9, 0)
t2 = (6, 7, 8)
print(t1+t2)

# to add all element inside list and tuple
# sum()
l1 = (8, 9, 7, 6)
print(sum(t1))

# * sort tuple
t1 =(8, 9, 0 ,89,12)
print(tuple(sorted(t1)))
print(tuple(sorted(t1, reverse=True)))

# ? iterate based on elements
l1 = [9, 8, 0, 6, 5]
for i in range(0, 5):
    print(l1[i])

# * iterate based on elements
l1 = [9, 8, 0, 6, 5]
for i in l1:
       print(i)

# ! -----> strings
s1 = "u"
print(type(s1))

s1 = "hello world"
# To access string
print(s1)
# indexing and slicing ----> same as list and tuple
print(s1[0:5])

# ----> common functions
# len(), min(), max(), index(), count()
s1 = "hello world"
print(len(s1))
print(min(s1))
print(max(s1))

# ord() --> used to find the ASCII value of a characte
s1 = 'u'
print(ord(s1))

# ! Functions of string
s1 = "hello world"

# Functions of string
s1 = "hello world"
#to convert all characters to upper case
print(s1.upper())

#to convert all characters to lower case
print(s1.lower())

# strip
s1 = "where are you?"
print(s1.lstrip())
print(s1.rstrip())
print(s1.strip())

#split() --> to split the words in string based on a character
s1 = "where are you?"
print(s1.split(" "))

# * replace() ---> to replace a specific char in the string
s1 = "where arte you?"
print(s1.replace('r', '&&'))

# 8 swapcase() ---> to convert capital to small and small capital at a time
s1 = "hey there"
print(s1.swapcase())

# title() ---> to write the string in format of title
s1 = 'never give up'
print(s1.title())

# capitalize()
s1 = 'never giveUP'
print(s1.capitalize())

# * join the strings
s1 = "hello"
s2 = 'world'
print(s1+s2)

s1 ='''how are you
iam fine
hey there
'''
# * Splilines() --> used to split the string based on lines
# print(s1.splitlines())

# find() ---> used to find the index based on a character
#s1 = "hello world"
#print(s1.find('z'))
#print(s1.index('z'))

# join() ---> 
l1 = ["hey", "there"]
print(" ".join(l1))
print("$".join(l1))

s1 = "Welcome to all"
print(s1.endswith('l'))
print(s1.startswith('W'))

s1 = "67"
print(type(s1))
print(s1.isdigit())

# * print string in reverse manner
s1 = "welcome to all"
print(s1[::-1])

# ! --->Eg:1
# wap to find the number of lower case letters
s1 = "HEY there you aRE"
for i.is lower():
       count+=1
      print("The total number of lower  case letters: ",count)


# ! ----> Eg:2 r ---> "$"
s1 = 'restarter'
# s1 = "IMAGIN"
fst = s1[0]
bal = s1[1:]
txt = bal.replace(fst, "$")
print(fst+txt)
PRINT(S1.replace('r',"$"))

# str = "bbbbbyyybbbaaioo"
# str2 = "%

# ! -----> Eg:3

Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
when an unknown printer took a galley of type and
scrambled it to make a type specimen book.It has survived not only five centuries,
but also the leap into electronic typesetting,remaining essentially unchanged.
It was popularised in the 1960s with the release of Letraset sheets
containing Lorem Ipsum passages, and more recently with desktop p


# chracters =len(s1)
# print(chraters)

# words =  s1.split(" ")
print(len(words))

sentences = s1.split('.')
for val in sentences:
    if val =='':
      index = sentenses.index(' ')
      sentyenses.pop(index)
print(len(sentenses))

space = 0
for val in s1:
    if val ==" ":
        space=space+1
print(space)

# 1.) Python program to capitalize the first and last character of each 
# word in a string
# 2.) Input : 128
# Output : Yes
# 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# 3.)l1=[1,2,3,4], l2=[5,6,7,8]
# Add both l1 and l2, ans=[6, 8, 10, 12]
        
