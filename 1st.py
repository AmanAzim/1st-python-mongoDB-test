print('hello')

if 5>2:
 print("five is greater than two")


x=10
y="hello"
print('x=',x,'y=',y)
print(x)

#This is a comment

"""
This is a comment
written in
more than just one line
"""

x,y,z="aman","tansen","roza"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

x = "awesome"
print("Python is " + x)

x=2
y=2
print(x+y)

x = 5
y = "John"
#cannot add string and numbers print(x + y)



x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))


x = 1 # int
y = 2.8 # float
z = 1j # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

for x in "mango":
    print(x)


#convert from int to complex:
c =4

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


import random
print(random.randrange(1,10))

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
print(x,y,z)
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
print(x,y,z,w)
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
print(x,y,z)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


#Substring. Get the characters from position 2 to position 5 (not included):
a="Hello"
print(a[2:4]) #wil print > ll
#The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip())

#The len() method returns the length of a string:
print(len(a))

#The lower() method returns the string in lower case:
print(a.lower())
#The upper() method returns the string in upper case:
print(a.upper())

#The replace() method replaces a string with another string:
print(a.replace("H", "J"))
print(a)

#The split() method splits the string into substrings if it finds instances of the separator:
print(a.split(','))


# we cannot combine strings and numbers
# we can combine strings and numbers by using the format() method!
#The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
age1 = 27
age2 = 31
txt = "My name is John, and I am {} no actually {} years old"
print(txt.format(age1,age2))

#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
# returns True because z is the same object as x
print(x is y)
# returns False because x is not the same object as y, even if they have thew same content
print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
print("apple" in x)
print("mango" not in x)
# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y
print(x != y)


thislist = ["apple", "banana", "cherry"]
print(thislist)
print(thislist[0])

text="the pruit is {}"
for x in thislist:
    print(text.format(x))


if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

print(len(thislist))

thislist.append("Orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "Orange")
print(thislist)

thislist.remove("banana")
print(thislist)

thislist.pop(1)
print(thislist)

#Make a copy of a list with the copy() method:
#mylist = thislist.copy()
#print(mylist)

#A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
myTuple=("aman","tansen","roza")
print(myTuple[0])

#A set is a collection which is unordered, unchangable(but addable) and unindexed. In Python sets are written with curly brackets.
mySet={"Car","House"}
print(mySet)
#You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
#But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
for x in mySet:
    print(x)
print("Car" in mySet)

#add item to set
mySet.add("Bike")
print(mySet)

#to add multiple items
mySet.update(["orange", "mango", "grapes"])

print(mySet)

#A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
myDict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(myDict["model"])

for x in myDict:
    print(x)

for x, y in myDict.items():
  print(x, y)

myDict["color"]="red"
print(myDict)

i=1
while i<6:
    print(i)
    i+=1

#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for x in range(6):
  print(x)

#The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter:
for x in range(2, 30, 3):
  print(x)

#The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for x in "apple":
    print(x)
else:
    print("Finally finished!")


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#functions
def myFun():
    print("Hello from a function")
myFun()


text = "I am {}"
def myFun2(pram):
    #print(pram+" is a parameter")
    print(text.format(pram))
myFun2("Aman")
myFun2(2)

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()


def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#recursion
def tri_recursion(pram):
    if pram > 0:
       result=pram+tri_recursion(pram-1)
       print(result)
    else:
       result=0
    return result


print("\n\nRecursion Example Results")
tri_recursion(3)

print("\n\n")
#A lambda function can take any number of arguments, but can only have one expression.
x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))


print("\n\n")

#class

class myClass:
    x=5
p1=myClass
print(p1.x)

print("\n\n")

class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def myfunc(self):
        print("Hello my name is " + self.name)

p2=Person("Aman", 31)
print(p2.name)
print(p2.age)
p2.myfunc()

#Inheritance #Create a Child Class #To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:
class Student(Person):
    pass # Use the pass keyword when you do not want to add any other properties or methods to the class.

x = Student("Mike", "Olsen")
x.myfunc()

class Student2(Person):
  def __init__(self, name, age, year):
    Person.__init__(self, name, age)
    self.graduationyear = 2019

  def welcome(self):
      print("Welcome", self.name, self.age, "to the class of", self.graduationyear)

x = Student2("Roza", "Babu", 2019)
print(x.graduationyear)
print(x.name)
x.welcome()


print("\n\n")
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

print("\n\n")




import datetime

x = datetime.datetime.now()
print(x)


print("\n\n")
#This method capitalizes the first letter of each word.

import camelcase

c = camelcase.CamelCase()

txt = "lorem ipsum dolor sit amet"

print(c.hump(txt))



try:
  print(g)
except:
  print("An exception occurred")



try:
  print(x)
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

finally:
  print("The 'try except' is finished")


print("\n\n")
#Taking input
print("Enter your name:")
x = raw_input()
print("Hello ", x)