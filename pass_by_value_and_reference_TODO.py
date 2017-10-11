import sys

def fooImmutable(a):
    print "\nReference count inside function: ", sys.getrefcount(a)
    print "\nValue Inside Function: ", a
    print "\nId inside function call: ", id(a)
    a = 3
    print "\nValue after update: ", a
    print "\nId after value update: ", id(a)

b = 5
print "\nValue Before Function Call: ", b
print "\nId Before Function Call: ", id(b)
print "\nReference count before function: ", sys.getrefcount(b)
fooImmutable(b)
print "\nValue after Function Call: ", b
print "\nId after Function Call: ", id(b)
print "\nReference count after function: ", sys.getrefcount(b)

'''
Output:

Value Before Function Call:  5

Id Before Function Call:  15335672

Reference count before function:  24

Reference count inside function:  26

Value Inside Function:  5

Id inside function call:  15335672

Value after update:  3

Id after value update:  15335720

Value after Function Call:  5

Id after Function Call:  15335672

Reference count after function:  24
'''

print "\n########################### String #####################################################\n"

c = 'abc'
print "\nValue Before Function Call: ", c
print "\nId Before Function Call: ", id(c)
print "\nReference count before function: ", sys.getrefcount(c)
fooImmutable(c)
print "\nValue after Function Call: ", c
print "\nId after Function Call: ", id(c)
print "\nReference count after function: ", sys.getrefcount(c)