# -*- coding: utf-8 -*-
import sys
'''
When an object’s reference count reaches zero, it is garbage-collected. However, in
some cases a circular dependency may exist among a collection of objects that are no
longer in use. Here’s an example:
'''

a = {}
print sys.getrefcount(a)
# Output: 2

b = {}
print sys.getrefcount(a)
# Output: 2
print sys.getrefcount(b)
# Output: 2

a['b'] = b
print sys.getrefcount(a)
# Output: 2
print sys.getrefcount(b)
# Output: 3

b['a'] = a
print sys.getrefcount(a)
# Output: 3
print sys.getrefcount(b)
# Output: 3

del a
print sys.getrefcount(b)
# Output: 3

del b
print sys.getrefcount(a)
# Name 'a' is not defined
print sys.getrefcount(b)
# Name 'b' is not defined

'''
In this example, the del statements decrease the reference count of a and b and destroy
the names used to refer to the underlying objects. However, because each object con-
tains a reference to the other, the reference count doesn’t drop to zero and the objects
remain allocated (resulting in a memory leak).To address this problem, the interpreter
periodically executes a cycle detector that searches for cycles of inaccessible objects and
deletes them.The cycle-detection algorithm runs periodically as the interpreter allocates
more and more memory during execution.The exact behavior can be fine-tuned and
controlled using functions in the gc module
'''