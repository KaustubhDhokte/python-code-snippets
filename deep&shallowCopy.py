'''
Two types of copy operations are applied to container objects such as lists and dictionaries:
a shallow copy and a deep copy. A shallow copy creates a new object but populates
it with references to the items contained in the original object.
'''

a = [1, 2, [8, 9], 5]
print id(a)
# Output: 47839472
b = list(a)

print b
# Output: [1, 2, [8, 9], 5]
print id(b)
# Output: 47858872
# Object Id changes

a[0] = 100
print a
# Output: [100, 2, [8, 9], 5]
print b
# Output: [1, 2, [8, 9], 5]

a.append(30)
print a
# Output: [100, 2, [8, 9], 5, 30]
print b
# Output: [1, 2, [8, 9], 5]

a[1] += 3
print a
# Output: [100, 5, [8, 9], 5, 30]
print b
# Output: [1, 2, [8, 9], 5]

a[2][1] = 10
print a
# Output: [100, 5, [8, 10], 5, 30]
print b
# Output: [1, 2, [8, 10], 5]

b[2][0] = 11
print a
# Output: [100, 5, [11, 10], 5, 30]
print b
# Output: [1, 2, [11, 10], 5]

'''
In this case, a and b are separate list objects, but the elements they contain are shared.
Therefore, a modification to one of the elements of a also modifies an element of b, as
shown.
'''

'''
A deep copy creates a new object and recursively copies all the objects it contains.
There is no built-in operation to create deep copies of objects. However, the
copy.deepcopy() function in the standard library can be used.
'''

import copy
a = [1, 2, [3, 4]]
b = copy.deepcopy(a)
print id(a)
# Output: 44433160
print id(b)
# Output: 44394576

a[2][1] = 6
print a
# Output: [1, 2, [3, 6]]
print b
# Output: [1, 2, [3, 4]]

b[2][0] = 8
print a
# Output: [1, 2, [3, 6]]
print b
# Output: [1, 2, [8, 4]]