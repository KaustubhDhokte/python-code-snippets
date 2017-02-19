# -*- coding: utf-8 -*-

class InheritedInteger(int):
    pass

a = InheritedInteger(3)

print type(a)
# Output: <class '__main__.InheritedInteger'>

print type(a) == type(4)
# Output: False

print isinstance(a, int)
# Output: True

print type(a) == int
# Output:False

'''
Because the isinstance() function is aware of inheritance, it is the preferred way to
check the type of any Python object.
Although type checks can be added to a program, type checking is often not as use-
ful as you might imagine. For one, excessive checking severely affects performance.
Second, programs don’t always define objects that neatly fit into an inheritance hierar-
chy. For instance, if the purpose of the preceding isinstance(s,list) statement is to
test whether s is “list-like,” it wouldn’t work with objects that had the same program-
ming interface as a list but didn’t directly inherit from the built-in list type.
'''