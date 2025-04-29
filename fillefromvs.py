#Hope to train more and more.
#0108615840 Mwebi
# This program adds up integers that have been passed as arguments in the command line
import sys
try:
    total = sum(int(arg) for arg in sys.argv[1:])
    print ('sum =', total)
except ValueError:
    print ('Please supply integer arguments')
print(" hi there...")
id=input(' what is your id \n')
print(" my id is "+id)
def add (a,b):
    return a*b;
ans=add(100,200)
print(" answer "+str(ans))
# Multipy
def multipy()
