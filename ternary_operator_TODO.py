'''
Yes, it was added in version 2.5.
The syntax is:

a if condition else b
First condition is evaluated, then either a or b is returned based on the Boolean value of condition
If condition evaluates to True a is returned, else b is returned.

For example:

>>> 'true' if True else 'false'
'true'
>>> 'true' if False else 'false'
'false'
Keep in mind that it's frowned upon by some Pythonistas for several reasons:

The order of the arguments is different from many other languages (such as C, Ruby, Java, etc.),
which may lead to bugs when people unfamiliar with Python's "surprising" behaviour use it 
(they may reverse the order).
Some find it "unwieldy", since it goes contrary to the normal flow of thought 
(thinking of the condition first and then the effects).
Stylistic reasons.
If you're having trouble remembering the order, then remember that if you read it out loud, you (almost) say what you mean.
For example, x = 4 if b > 8 else 9 is read aloud as x will be 4 if b is greater than 8 otherwise 9.
'''