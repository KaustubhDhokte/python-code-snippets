# The enumerate() function adds a counter to an iterable.

#So for each element in cursor, a tuple is produced with (counter, element); the for loop binds that to row_number and row, respectively.


elements = ['foo', 'bar', 'baz']

for element in elements:
    print element

"""
Output: 
foo
bar
baz
"""

for element in enumerate(elements):
    print element

"""
output:
(0, 'foo')
(1, 'bar')
(2, 'baz')
"""

for element in enumerate(elements, 56):
    print element

"""
Output
(56, 'foo')
(57, 'bar')
(58, 'baz')
"""
