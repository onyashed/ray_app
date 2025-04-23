# Python basics
# This is a single line comment.

"""
Block comments goes in here.
another line goes underneath here.
"""
# from py_datatypes import dictdata
age=0;
# Simple output to screen
print('Hello, world!')
# Simple input into system from keyboard.
name = input('What is your name?\n')
# Response back from system with input details displayed.
print('Hi, %s.' % name)
# Simple void method with a single parameter.
age=input(" What is your age?\n")
print(" You sre "+age+ " years old.")
if age != 18:
    print(" You are allowed to vote.")
else:
    print(" You are ineligible ")


def greet(name):
    print ('Hello', name)



#Triangle Area

def triarea(base,height): # Function head
    return 0.5*base*height;
#call the function to execute or run
print('The area is %f'+triarea(12,6))
# dictdata=dict()
# dictdata={'product':{{'item':'Soap'},{'brand':'Geisha'},{'weight':20},{'capacity':'grammes'}}}
# print(dictdata.items())
greet('Sitini')
greet('Under Pressure.')
greet('Nabukwesi')
# Arithmetic operators
# Addition
def add( a,  b):
    return a+b;

# the parameters need not be datatyped.
print(add(1.1,2.90))
def div(a,b):
    if a > 18:
        return a/b;
    else:
        print (" infinity")


print(div(0,2))
# Handle Mul, sub and modulus functions.
