# Python basics
# This is a single line comment.

"""
Block comments goes in here.
another line goes underneath here.
"""
# Simple output to screen
print('Hello, world!')
# Simple input into system from keyboard.
name = input('What is your name?\n')
# Response back from system with input details displayed.
print('Hi, %s.' % name)
# Simple void method with a single parameter.
def greet(name):
    print ('Hello', name)

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
    if b==0:
        print (" infinity")
    else:
        return a/b;
print(div(0,2))
# Handle Mul, sub and modulus.
