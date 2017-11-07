def div1(x,y):
    print "%s/%s = %s" % (x, y, x/y)
    
def div2(x,y):
    print "%s//%s = %s" % (x, y, x//y)

div1(5,2)
div1(5.,2)
div2(5,2)
div2(5.,2.)

'''
In Python 2, the output of the above code will be:

5/2 = 2
5.0/2 = 2.5
5//2 = 2
5.0//2.0 = 2.0
By default, Python 2 automatically performs integer arithmetic if both operands are integers.
As a result, 5/2 yields 2, while 5./2 yields 2.5.

Note that you can override this behavior in Python 2 by adding the following import:

from __future__ import division
Also note that the “double-slash” (//) operator will always perform integer division, 
regardless of the operand types. That’s why 5.0//2.0 yields 2.0 even in Python 2.

Python 3, however, does not have this behavior; i.e., 
it does not perform integer arithmetic if both operands are integers. 
Therefore, in Python 3, the output will be as follows:

5/2 = 2.5
5.0/2 = 2.5
5//2 = 2
5.0//2.0 = 2.0
'''

'''
	
In Python 3, they made the / operator do a floating-point division,
and added the // operator to do integer division (i.e. quotient without remainder);
whereas in Python 2, the / operator was simply integer division, 
unless one of the operands was already a floating point number.

In Python 2.X:

>>> 10/3
3
>>> # to get a floating point number from integer division:
>>> 10.0/3
3.3333333333333335
>>> float(10)/3
3.3333333333333335
In Python 3:

>>> 10/3
3.3333333333333335
>>> 10//3
3

'''