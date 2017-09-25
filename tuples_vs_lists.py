'''
Tuples are immutable, and usually contain an heterogeneous sequence of elements that are accessed via unpacking (see later in this section) or indexing (or even by attribute in the case of namedtuples).
Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.
'''
'''
Lists are for looping, tuples are for structures i.e. "%s %s" %tuple.
Lists are usually homogeneous, tuples are usually heterogeneous.
Lists are for variable length, tuples are for fixed length.
'''
# https://stackoverflow.com/questions/626759/whats-the-difference-between-lists-and-tuples

a = (1, 2, 3)
print a[0]
# Output: 1

print a[0:2]

a[1] = 3
# TypeError: 'tuple' object does not support item assignment

print a