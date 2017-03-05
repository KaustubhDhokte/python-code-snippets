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