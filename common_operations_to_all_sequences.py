s1 = [1, 2, 4, 10, 12]
s2 = "foobar"

print s1[0]
# Output: 1

print s1[-1]
# Output: 12

print s1[-2]
# Output: 10

print s1[-3]
# Output: 4

print s1[-4]
# Output: 2

print s1[-5]
# Output: 1

#print s1[5]
# Output: IndexError: list index out of range

print s2[0]
# Output: f

print s2[-1]
# Output: r

print s2[-2]
# Output: a

print s2[-3]
# Output: b

print s2[-4]
# Output: o

print s2[-5]
# Output: o

#print s2[6]
# Output: IndexError: String index out of range

print s1[0:2]
# Output: [1, 2]

print s1[0:8]
# Output: [1, 2, 4, 10, 12]

print s1[-8:0]
# Output: []

print s2[0:80]
# Output: foobar

print s1[0:4]
# Output: [1, 2, 4, 10]

print s1[4:2]
# Output: []

print s1[2:4]
# Output: [4, 10]

print s1[2:8]
# Ouput: [4, 10, 12]

print s1[0:4:2]
# Output: [1, 4]

print s1[0:4:1]
# Output: [1, 2, 4, 10]

print s1[::]
# Output: [1, 2, 4, 10, 12]

print s1[0:4:-2]
# Output: []

print s1[0::-2]
# Output: [1]

print s1[0:]
# [1, 2, 4, 10, 12]

print s2[:3]
# foo

print s2[:3:2]
# fo

print s2[:3:-1]
# ra

print s2[:3:-2]
# r

print len(s2), len(s1)
# 6 5

print max(s1), max(s2)
# 12 r

print min(s1), min(s2)
# 1 a

print all(s1), all(s2)
# True True
# Check whether all items in list are True

s1.append(0)

print all(s1)
# False

print any(s1), any(s2)
# True True
# Check whether any item in list is True

print sum(s1)
# 29

#print sum(s2)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

del s1[2]

print s1[len(s1)-1]

# print s1[10]: index out of range
print s1[10:] # Empty list

# print s1[-10] # IndexError

a = [1, 2, 3, 4, 5]
print a[::2] # 1, 3, 5