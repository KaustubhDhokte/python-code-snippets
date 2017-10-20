'''
Python uses the word :- "Magic Methods" because, those methods really performs magic for you program. One of the biggest advantages of using Python's magic methods is that they provide a simple way to make objects behave like built-in types. That means you can avoid ugly, counter-intuitive, and nonstandard ways of performing basic operators.

Consider a following example :-

dict1 = {1 : "ABC"}
dict2 = {2 : "EFG"}

dict1 + dict2
Traceback (most recent call last):
  File "python", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
This gives an error, because dictionary type doesn't support addition. Now, let's extend dictionary class and add "__add__" magic method :-

class AddableDict(dict):

    def __add__(self, otherObj):
        self.update(otherObj)
        return AddableDict(self)


dict1 = AddableDict({1 : "ABC"})
dict2 = AddableDict({2 : "EFG"})

print (dict1 + dict2)
Now, it gives following output,

{1: 'ABC', 2: 'EFG'}
Thus, by adding this method, suddenly magic has happened and the error you were getting earlier, has gone away.
'''