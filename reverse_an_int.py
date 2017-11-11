#!/usr/bin/env python
# Method1
'''
a = 546
print a
astr = list(str(a))
l = len(astr)-1
for i in range(0, l):
    astr[i], astr[l-i] = astr[l-i], astr[i]
ln = ''.join(astr)
a = int(ln)
print a
'''

# Method2:-Simplest
print int(str(265)[::-1])

