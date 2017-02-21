i = 3
print id(i)
# Output: 40926520

i += 5
print id(i)
# Output: 40926460

# Hence int is an immutable object. Its identity changes with the value.

j = 'abc'
print id(j)
# Output: 40536064

j += 'pqr'
print j
# Output: abcpqr
print id(j)
# Output: 39711072

# Hence string is an immutable object. Its identity changes with the value.

k = True
print id(k)
# Output: 491730004

k = k & False
print k
# Output: False
print id(k)
# Output: 491729796

# Hence bool is an immutable object. Its identity changes with the value.

a = [1, 2, 3]
print id(a)
# Output: 43514096
a[0] = 4
print id(a)
# Output: 43514096

# Hence list is mutable object. Its identity does not change with the value. Same stands true for dicts