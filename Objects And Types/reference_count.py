# -*- coding: utf-8 -*-
import sys

'''
An object’s reference count is decreased by the del statement or whenever a refer-
ence goes out of scope (or is reassigned)
'''

class MyClassInheritedFromObjectClass(object):
    def __init__(self):
        pass

class MyClass():
    def __init__(self):
        pass

a = 3
b = 3

print sys.getrefcount(a)
# Output : 31
'''
In many cases, the reference count is much higher than you might guess. For immutable
data such as numbers and strings, the interpreter aggressively shares objects between dif-
ferent parts of the program in order to conserve memory.
'''

########################################################################################################################
# SOMETHING LITTLE OUT OF CONTEXT
m = MyClass
print type(m)
# Output: <type 'classobj'>

m = MyClass()
print type(m)
# Output: <type 'instance'>

obj = MyClassInheritedFromObjectClass
print type(obj)
# Output: <type 'type'>

obj1 = MyClassInheritedFromObjectClass()
print type(obj)
# Output: <class '__main__.MyClassInheritedFromObjectClass'>
########################################################################################################################

print sys.getrefcount(obj1)
# Output: 2

del obj1

#print sys.getrefcount(obj1)
# Output: NameError: name 'obj1' is not defined

obj1 = MyClassInheritedFromObjectClass()
obj2 = MyClassInheritedFromObjectClass()

print sys.getrefcount(obj1)
# Output: 2

print  sys.getrefcount(obj2)
# Output: 2

print id(obj1)
# Output: 140312278725136
print id(obj2)
# Output: 140312278725200

import gc
print gc.get_referents(obj1)
#[<class '__main__.MyClassInheritedFromObjectClass'>]

obj2 = obj1
print  sys.getrefcount(obj1)
# Output: 3
print  sys.getrefcount(obj2)
# Output: 3

a = 37
print sys.getrefcount(a)
# Output: 9

b = a
print sys.getrefcount(a)
# Output: 10
print sys.getrefcount(b)
# Output: 10

c = 23
print sys.getrefcount(c)
# Output: 13

a = c
print sys.getrefcount(c)
# Output: 14
print sys.getrefcount(a)
# Output: 14
print sys.getrefcount(b)
# Output 9