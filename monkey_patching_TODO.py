# TODO: Example
# https://stackoverflow.com/questions/5626193/what-is-monkey-patching
'''
For instance, consider a class that has a method get_data.
This method does an external lookup (on a database or web API, for example), and various other methods in the class call it.
However, in a unit test, you don't want to depend on the external data source - so you dynamically replace the get_data method with a stub that returns some fixed data.

Because Python classes are mutable, and methods are just attributes of the class,
you can do this as much as you like - and, in fact, you can even replace classes and functions in a module in exactly the same way.
'''
'''
A MonkeyPatch is a piece of Python code which extends or modifies other code at runtime (typically at startup).
'''

'''
According to Wikipedia:
In Python, the term monkey patch only refers to dynamic modifications of a class or module at runtime, 
motivated by the intent to patch existing third-party code as a workaround to a bug or feature which does not act as you desire.
'''