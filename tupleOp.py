a = tuple()
a = (5, 7, 'b', 7, 6, 7, 8, 9, 10)
b = (2, 3, 9)
print a.count(7)
# Op: 3
print id(a)
# 139800498676944
print id(b)
# 139800498690720
print a.index(7)
# 1
print a[0]
# 5
a[0] = 8
# TypeError: 'tuple' object does not support item assignment
print a == b
# False
a = b
print a
print b
print id(a)
print id(b)

