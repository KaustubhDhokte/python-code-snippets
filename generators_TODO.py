# Solve problems given here: http://anandology.com/python-practice-book/iterators.html
# https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
# Modify generators usage by adding an example from above link
def gen():
    pass

g = gen
print g

def gen2(n):
    print "Before loop"
    for i in range(n):
        print "Inside loop, before yeild", i
        yield i
        print "Inside loop, after yeild", i

g1 = gen2
print g1

g2 = gen2(5)
print g2

print g2.next()
'''
OutPut:
Before loop
Inside loop, before yeild 0
0
'''

print g2.next()
'''
Output:
Inside loop, after yeild 0
Inside loop, before yeild 1
1
'''
print g2.next()
'''
Inside loop, after yeild 1
Inside loop, before yeild 2
2
'''

print g2.next()
'''
Inside loop, after yeild 2
Inside loop, before yeild 3
3
'''

print g2.next()
'''
Inside loop, after yeild 3
Inside loop, before yeild 4
4
'''

print g2.next()
'''
Inside loop, after yeild 4
Traceback (most recent call last):
  File "generators.py", line 25, in <module>
    print g2.next()
StopIteration
'''
