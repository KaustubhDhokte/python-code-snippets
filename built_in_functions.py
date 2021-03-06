# -*- coding: utf-8 -*-

#http://www.bogotobogo.com/python/python_functions_built_in.php
#https://docs.python.org/2/library/functions.html

######################################## abs() ##############################################################
a = [4, 5.6, 0, -13, -14.39, 'a', 'random_string', complex(3, 4), 'i', complex(4, -5)]
for i in a:
    # print abs(a) : Output: TypeError: bad operand type for abs(): 'list'
    # For string inputs: TypeError: bad operand type for abs(): 'str'
    if not isinstance(i, str):
        print abs(i)
    # Output: 4, 5.6, 0, 13, 14.39, 5.0, 6.40312423743
####################################################################################################################################################

######################################### all() ####################################################################################################
a = [[False], [True], [True, False], [True, True], [1, 0], [0], [1], [], ['rand_string'], 
        [5.7], {'a':5}, {0:0}, {0:3}, {4:0} ,{}, 1]

for i in a:
    try:
     print all(i)
    except TypeError, e:
        print("Exception occurred: " + str(e) + " " + e.message) # Prints same exception twice

# Output:
# False, True, False, True, False, False, True, True, True, True, True, False, False, True, True
# Exception occurred: 'int' object is not iterable 'int' object is not iterable
###################################################################################################################

################################################### any() ###########################################################

a = [[False], [True], [True, False], [True, True], [1, 0], [0], [1], [], ['rand_string'], 
        [5.7], {'a':5}, {0:0}, {0:3}, {4:0} ,{}, {5:5, 0:9}, 1]
print ("\n any() \n")
for i in a:
    try:
     print any(i)
    except TypeError, e:
        print("Exception occurred: " + str(e) + " " + e.message) # Prints same exception twice

# Output:
# False True True True True False True False True True True False False True False True
# Exception occurred: 'int' object is not iterable 'int' object is not iterable
##########################################################################################################################

################################################# bool() #################################################################

a = [0, 1, -1, 'atr', 'v', 5.8, -4.3, [], [True], [False], [1], [0], [1, 0], {}, {3:2, 0:2} ]
print "\n bool() \n"
for i in a:
    try:
     print bool(i)
    except TypeError, e:
        print("Exception occurred: " + str(e) + " " + e.message) # Prints same exception twice

# Output:
# False True True True True True True False True True True True True False True

print type(True) # <type 'bool'>
print type(False) # <type 'bool'>

#class MyBool(bool):
#    pass
# TypeError: Error when calling the metaclass bases
#    type 'bool' is not an acceptable base type

################################################################################################################

############################################ callable #########################################################
print "\nCallable\n"
l = [str, 1, 'i', 2.7, [5,4], {3:4}, (2, 3)]
for i in l:
    print callable(i)


'''
A callable is anything that can be called.

The built-in callable (PyCallable_Check in objects.c) checks if the argument is either:

an instance of a class with a __call__ method or
is of a type that has a non null tp_call (c struct) member which indicates callability otherwise (such as in functions, methods etc.)
The method named __call__ is (according to the documentation)

Called when the instance is ''called'' as a function
Example

class Foo:
  def __call__(self):
    print 'called'

foo_instance = Foo()
foo_instance() #this is calling the __call__ method

'''


# Output: True False False False False False False
#############################################################################################################

################################################## cmp() ######################################################

print "\ncmp()\n"
class MyClass(object):
    pass

m1 = MyClass()
m2 = MyClass()
m3 = m2

dct = {'i':'i', 'i':'I', 'i':1, 1:1, 1:2, m1:m2, m2:m3}

for k,v in dct.iteritems():
    print k, v
    print cmp(k, v)
#############################################################################################################

############################################# delattr() #######################################################

print "\n delattr() \n"

class MyClass():
    def __init__(self):
        self.a = 4
    def getA(self):
        return self.a

m = MyClass()
print m.getA()
delattr(m, 'a')
#print m.getA()

'''
Output:
4
Traceback (most recent call last):
  File "built_in_functions.py", line 132, in <module>
    print m.getA()
  File "built_in_functions.py", line 127, in getA
    return self.a
AttributeError: MyClass instance has no attribute 'a'
'''

###########################################################################################################

##################################################### enumerate() #########################################

# Return an enumerate object.
print "enumerate()\n"

l1 = [2, 4, 6, 7, 'a', [4,3], {0:3, 9:2}]
targets = [l1, 1, 'b']

for t in targets:
    try:
        print enumerate(t) #<enumerate object at 0x7f68ad8f78c0>
        print list(enumerate(t))
    except TypeError:
        pass
    # [(0, 2), (1, 4), (2, 6), (3, 7), (4, 'a'), (5, [4, 3]), (6, {0: 3, 9: 2})]

###########################################################################################################

############################################### eval() ####################################################
x = 3
print eval('x')
###########################################################################################################

################################################### globals() #############################################

print globals()

'''
{'MyClass': <class __main__.MyClass at 0x7f5949aea668>, 'targets': [[2, 4, 6, 7, 'a', [4, 3], {0: 3, 9: 2}], 1, 'b'],
 '__package__': None, 'm1': <__main__.MyClass object at 0x7f5949b03450>, 'm3': <__main__.MyClass object at 0x7f5949b0
3550>, 'm2': <__main__.MyClass object at 0x7f5949b03550>, '__doc__': None, '__warningregistry__': {('BaseException.me
ssage has been deprecated as of Python 2.6', <type 'exceptions.DeprecationWarning'>, 40): True, ('BaseException.messa
ge has been deprecated as of Python 2.6', <type 'exceptions.DeprecationWarning'>, 24): True}, '__builtins__': <module
 '__builtin__' (built-in)>, '__file__': 'built_in_functions.py', 'l1': [2, 4, 6, 7, 'a', [4, 3], {0: 3, 9: 2}], '__na
me__': '__main__', 'dct': {'i': 1, 1: 2, <__main__.MyClass object at 0x7f5949b03450>: <__main__.MyClass object at 0x7
f5949b03550>, <__main__.MyClass object at 0x7f5949b03550>: <__main__.MyClass object at 0x7f5949b03550>}, 'a': [0, 1,
-1, 'atr', 'v', 5.8, -4.3, [], [True], [False], [1], [0], [1, 0], {}, {0: 2, 3: 2}], 'e': TypeError("'int' object is
not iterable",), 'i': (2, 3), 'k': <__main__.MyClass object at 0x7f5949b03550>, 'm': <__main__.MyClass instance at 0x
7f5949af8878>, 'l': [<type 'str'>, 1, 'i', 2.7, [5, 4], {3: 4}, (2, 3)], 't': 'b', 'v': <__main__.MyClass object at 0
x7f5949b03550>, 'x': 3}
'''

##########################################################################################################

################################################### getattr() ############################################
m2 = MyClass()
print getattr(m2, 'a')
print hasattr(m2, 'b')
print hasattr(m2, 'a')

c = [1, 2, 3, 4]
print hasattr(c, 'd')

##########################################################################################################




'''
TO DO: Study following built-in functions

bytearray 

bytes

callable

classmethod

compile

complex

dir

divmod 
 
exec 

filter 

float

format

frozenset 


id

input 

isinstance 

issubclass 

iter 

len 

locals 

map 

max 

memoryview 

min 

next 

open 

pow

property 

range

repr 

reversed  

set 

setattr 

slice 

sorted 

staticmethod 

str 

sum 

super 

tuple 

type 

vars 

zip 

__import__
'''