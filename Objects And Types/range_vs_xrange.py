# https://stackoverflow.com/questions/135041/should-you-always-favor-xrange-over-range
# https://stackoverflow.com/questions/94935/what-is-the-difference-between-range-and-xrange-functions-in-python-2-x

'''
It is for optimization reasons.

range() will create a list of values from start to end (0 .. 20 in your example). This will become an expensive operation on very large ranges.

xrange() on the other hand is much more optimised. it will only compute the next value when needed (via an xrange sequence object) and does not create a list of all values like range() does.
'''

'''
range creates a list, so if you do range(1, 10000000) it creates a list in memory with 9999999 elements.

xrange is a sequence object that evaluates lazily.
'''

'''
For performance, especially when you're iterating over a large range, xrange() is usually better. However, there are still a few cases why you might prefer range():
In python 3, range() does what xrange() used to do and xrange() does not exist. If you want to write code that will run on both Python 2 and Python 3, you can't use xrange().
range() can actually be faster in some cases - eg. if iterating over the same sequence multiple times.  xrange() has to reconstruct the integer object every time, but range() will have real integer objects. (It will always perform worse in terms of memory however)
xrange() isn't usable in all cases where a real list is needed. For instance, it doesn't support slices, or any list methods.
[Edit] There are a couple of posts mentioning how range() will be upgraded by the 2to3 tool. For the record, here's the output of running the tool on some sample usages of range() and xrange()
'''

'''
No, they both have their uses:
Use xrange() when iterating, as it saves memory. Say:
for x in xrange(1, one_zillion):
rather than:
for x in range(1, one_zillion):
On the other hand, use range() if you actually want a list of numbers.
multiples_of_seven = range(7,100,7)
print "Multiples of seven < 100: ", multiples_of_seven
'''


'''
You will find the advantage of xrange over range in this simple example:

import timeit

t1 = timeit.default_timer()
a = 0
for i in xrange(1, 100000000):
    pass
t2 = timeit.default_timer()

print "time taken: ", (t2-t1)  # 4.49153590202 seconds

t1 = timeit.default_timer()
a = 0
for i in range(1, 100000000):
    pass
t2 = timeit.default_timer()

print "time taken: ", (t2-t1)  # 7.04547905922 seconds
The above example doesn't reflect anything substantially better in case of xrange.

Now look at the following case where range is really really slow, compared to xrange.

import timeit

t1 = timeit.default_timer()
a = 0
for i in xrange(1, 100000000):
    if i == 10000:
        break
t2 = timeit.default_timer()

print "time taken: ", (t2-t1)  # 0.000764846801758 seconds

t1 = timeit.default_timer()
a = 0
for i in range(1, 100000000):
    if i == 10000:
        break
t2 = timeit.default_timer() 

print "time taken: ", (t2-t1)  # 2.78506207466 seconds
With range, it already creates a list from 0 to 100000000(time consuming), but xrange is a generator and it only generates numbers based on the need, that is, if the iteration continues.

In Python-3, the implementation of the range functionality is same as that of xrange in Python-2, while they have done away with xrange in Python-3
'''