# we have 3 subject beggin1 , beggin2 and beggin3 than we can move to advanced guys
# python made by guido van roussum
# python is the automate programing language
# the codes written by ps4 spidey so it's open source and free software for begginers pythons
# first statement is print
print("Welcome to my app")
# guys this source code is availabe on the public domain that is https://ps4officialsourcecode.000webhostapp.com
# so you can get this source code from the link

# lets do it

# how to get the data type in python
# string
# int
# boolean
# float
# complex
# if you remove type and () you can get your value to print guys
print(type("WELCOME"))
print(type(23))
print(type(5j + 2))
print(type(True))
print(type(False))
print(type(23.3))

# you see but how can we change float or int in to string don't think to much

print(type("23"))
print(type("23.5"))

# how to line space 

# see this is very easy
# if you studied c or c++ you can undrestand it

print("Welcome guys \n")
print("This is having a space")

# now we are going to study variables in python so let's go
# see i comment the sample variable
# a = "PS4 GAMING"
# so let's print it

# you can diffrent name for your variable
# when your are creating a app you must give a unique variable name

# you can use underscore _ 
# but you cannot use numbers i mean int in the first letter
# so lets see

hello = "VALUE1"

print(hello)

number_one = 1
print(number_one)

numberTwo = 2
print(numberTwo)

# so you will understand how can we print strings, int , float , boolean and complex
# so let's another topic 
# comment # this is the comment simple i used it in every places

# so lets go to the class

# seee it is a sample comment
# it's must and it's in all programing languges

# let's go to anothe topic
# you can use this (.element and methds) so let's see this section i python

a = "ps4 gaming"

# but the value is in lowercase but i want to change upper case so let's seee

print(a.upper())
# it was change upper
# you can use lots of .elements iam always calling this .element if you can understand it very easily

# so you can practise it and you will get more ideas in python

# so we studied the basics in python than now we are going to study input()

# before we start our section let's see some sort notes 
# what is input? "input is get value from user" 
# how can we use input? you can use like this "input"

input("What is your name?")

# you can store it in a variable

val = input("What is your fname?")

# than you can use it every place in your app

print(val)

# you can call like this
print("My fname is"+ val)
print("My fname is ", val)

# you can with + or , but you must use a space when your using ,
# now we are going to see how to pring paragraph
# you thinks we can print like 
# print("hello 
# world
# but the time")

# this how to print strings in python

# 1. ""
#  2.''
#  3. """"""

# now we are going to print ""
print("hello")
#  now we are going to print ''
print('this is hello')

# this is special for paragraph """"""
print("""
1.ps4 gaming
2.password
3.cracker
4.hacker
""")

# if you run it it will give a value

# so we are going to def

# see a simple example for this one
# now i am going to print test par1 and part 2 marks
# and iam going get full marks
def testmarks(a , b):
    print(a+ b)

testmarks(10,20)

# now we are going to .strip and .split it's a simple method
# this is strip
e = " welcome"
print(e)
print(e.strip())

# this is split

a = "varibale"

print(a)
print(a.split())

# this class we show some beggining methods and practice it well

# and guys write this codes and practice the beggin 1

# now length in python

a = "Gamer"

print(len(a))

# mathametic operation in python

a = 10
b = 13
c = a+ b
print(c)
print(a + b)

# you can do all math operations in python so you can practise with my code guys

# we can equal with the variable

phone = 1200
phone2 = 1200

# but we can print it like this
phone1 = phone3 = 1200
# if you print it it will show the value
# and like this
a , b = 1200, 1200
c , d = 1200, 1300

# so if you print it it is the terrafy

# we can replace the words
game = "PS5 spidey"

print(game.replace("5","4"))
# and split this one

print(game.split("5"))
print("ps5" in game)

print(phone ** phone1)

print(100 > 10)
print(100 > 1000)
print(100 == 100)

# this is very easy bro

# now casting

x = str(10.10)
print(x)

# now we are going to see list
fruits = ['apple','orange','papaw']
# you can change the 1st value
fruits[1] = 'banana'
# you can append another thing
fruits.append("berry")
print(fruits)
 

 # tuples
# tuple cannot append guys
number = [11 , 12 ,13]
number.sort(reverse=True)
print(number)

# set
# set will change every
hero = {'iron','spider man','super man'}

# dictionary
# dictionary is using for save a user data guys
my_data = {
    "name":"PS4 SPIDEY",
    "age":"25"
}
print(my_data)

# you can change your age or name
# here a example
my_data["age"] = "14"
# you can get age or name from dictionary
print(my_data.get("age"))


# now we are going to study if elif else 
if 10 > 1:
    print("hello")
elif 10 == 11:
    print("welcome")
else:
    print("Sorry")

# you can change the value and practise

# now we are going to see loop
# there are 2 loops in python
# for loop
# while loop

# the loops are looping it's very easiest topice in python
name = "PS4 SPDIEY"
for letters in name:
     print(letters)
fruits = ['apple', 'orange', "game"]
for fruit in fruits:
     print(fruit)
for i in "hello,world":
     if i == ',':
          # if you remove the continue it will continue and break 
          # continue 
          print(", is present")
# break
else:
     print(", is not present")
# range
for number in range(10, 30, 4):
     print(number)
for number in range(5):
     print(number)
for i in range(2):
     print(i)
else:
     print('all numbers are finished')
# while loop will continue
# while loop
i = 1
while i < 5:
     print(i)
     i += 1
else:
     print('over')

# Lamda
# lambda function is like def 
# but lamda is easier than def
add_5 = lambda number : number + 10
print(add_5(10))

print(add_5(120))

# our class was over and if you can create a calculator using python
# if you know you can create a calculator

# simple calculator
def add(a, b):
     return a+b
def sub(a, b):
     return a-b
def mul(a, b):
     return a*b
def div(a, b):
     return a/b
print("""select operation
1.add
2.sub
3.mul
4.div
""")
choice = int(input("enter your choice"))
a = int(input("enter first number"))
b = int(input('enter second number'))
if choice == 1:
     print(add(a, b))
elif choice == 2:
     print(sub(a, b))
elif choice == 3:
     print(mul(a, b))
elif choice == 4:
     print(div(a, b))
else:
     print('enter correct choice')

# now our class was over than we can see the Intermative in python that is JSON
# so bye guys thank you to get my source code bye bye bye...