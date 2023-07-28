"""
Author: Onyango Edwin
email:onyango@verygood.co.ke
VeryGood Solutions."""
import datetime
import time
MONGODB_SETTINGS = {
	'DB' : 'raydb',
	'HOST' : '127.0.0.1',
	'PORT' : 27017
	}

# import MongoEngine
# db = MongoEngine()


# Control Structures tested within functions.

# if


def fnif(a):# Functions should be in lower case.
    if a>10:
        print('%s is  greater than 10' % a) # Concatenation python.


fnif(11)


def fnifelse(a):
    if(a>10):
        print('%s is  greater than 10' % a) # Concatenation python.
    else:
        print('%s is  less than 10' % a) # Concatenation python.
fnifelse(11)

# nested if
def whileloop(a):
    while(a>=10):
        print(a)
        a=a-1

def count(firstval=0, step=1):
    x = firstval
    while 1:
        yield x
        x += step

def ifelseif(names):
    if names == "A":
        now= time.time()
        print(now)
        #listfiles = os.listdir("docs/downloads/docs/conversions/swa/doc2txt")
    elif names == "B":
        ...
       # listfiles = os.listdir
    return names
ifelseif("A")

# For loop.
userlist=['Ray','Githinji','Sidera']
for user in userlist:
    print(user)