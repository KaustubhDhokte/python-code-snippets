compare(4, 6)
# Output: NameError: name 'compare' is not defined

def compare(a, b):
    if a is b:
        print "a and b are the same object"
    if a == b:
        print "a and b have the same value"
    if type(a) is type(b):
        print "a and b have the same type"


int1 = int(3)
int2 = int(5)
int3 = 3
float1 = float(5)
complex1 = complex(3, 5)
s1 = str("abc")
s2 = "xyz"

compare(int1, int2)
# Output: a and b have the same type

compare(int1, int3)
'''
Output:
a and b are the same object
a and b have the same value
a and b have the same type
'''

print id(int1)
print id(int3)
'''
Output:
41070888
41070888
'''

compare(int2, float1)
# Output: a and b have the same value
