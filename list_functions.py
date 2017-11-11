a = list()
b = [5, 6, 8, 8, 9]
print type(a)
print type(b)
print dir(a)
print dir(b)

print str(b)
print b.__str__()

'''
<type 'list'>
<type 'list'>
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '
__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__it
er__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reverse
d__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'cou
nt', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '
__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__it
er__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reverse
d__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'cou
nt', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
[5, 6, 8, 8, 9]
[5, 6, 8, 8, 9]
'''
a = [1,2,3,4]

b.append(10)
print b
# OP: [5, 6, 8, 8, 9, 10]
print b.count(8)
# 2
b.extend(a)
print b
# OP: [5, 6, 8, 8, 9, 10, 1, 2, 3, 4]

print len(b)
# 10

print b.index(8, 1, 7)
# 2

print b.index(8, 3, 7)
# 3

b.insert(0, 99)

print b
# OP: [99, 5, 6, 8, 8, 9, 10, 1, 2, 3, 4]

b.pop()
print b
# [99, 5, 6, 8, 8, 9, 10, 1, 2, 3]

b.remove(8)
print b
# Deletes 1st occerence [99, 5, 6, 8, 8, 9, 10, 1, 2, 3]

b.append(9)
b.append(9)
print b
# [99, 5, 6, 8, 9, 10, 1, 2, 3, 9, 9]

b.remove(9)
print b
# [99, 5, 6, 8, 10, 1, 2, 3, 9, 9]

b.reverse()
print b
# [9, 9, 3, 2, 1, 10, 8, 6, 5, 99]

b.sort()
print b
# [1, 2, 3, 5, 6, 8, 9, 9, 10, 99]

print b.__sizeof__()
# 176

c = list(set(b))
print c
print type(c)
# [1, 2, 3, 5, 6, 8, 9, 10, 99]
# <type 'list'>

