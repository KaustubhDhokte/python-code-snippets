# -*- coding: utf-8 -*-
'''
In C++ terminology, normally class members (including the data members) are public (except Private Variables and Class-local References),
and all member functions are virtual.

There are no shorthands for referencing the object’s members from its methods: 
the method function is declared with an explicit first argument representing the object, 
which is provided implicitly by the call. 

As in Smalltalk, classes themselves are objects. 
This provides semantics for importing and renaming. 

Unlike C++ and Modula-3, 
built-in types can be used as base classes for extension by the user. 

Also, like in C++, most built-in operators with special syntax (arithmetic operators, subscripting etc.)
can be redefined for class instances.
'''

'''
Objects have individuality, and multiple names (in multiple scopes) can be bound to the same object.
This is known as aliasing in other languages.
This is usually not appreciated on a first glance at Python, and can be safely ignored when dealing with immutable basic types (numbers, strings, tuples).
However, aliasing has a possibly surprising effect on the semantics of Python code involving mutable objects such as lists, dictionaries, and most other types.
This is usually used to the benefit of the program, since aliases behave like pointers in some respects.
For example, passing an object is cheap since only a pointer is passed by the implementation;
and if a function modifies an object passed as an argument, the caller will see the change — 
this eliminates the need for two different argument passing mechanisms as in Pascal.
'''

'''
A namespace is a mapping from names to objects. 
Most namespaces are currently implemented as Python dictionaries, but that’s normally not noticeable in any way (except for performance). 
Examples of namespaces are: the set of built-in names (containing functions such as abs(), and built-in exception names); 
the global names in a module; and the local names in a function invocation.
In a sense the set of attributes of an object also form a namespace.
The important thing to know about namespaces is that there is absolutely no relation between names in different namespaces; 
for instance, two different modules may both define a function maximize without confusion — users of the modules must prefix it with the module name.
'''

'''
Namespaces are created at different moments and have different lifetimes.
The namespace containing the built-in names is created when the Python interpreter starts up, and is never deleted.
The global namespace for a module is created when the module definition is read in; normally, module namespaces also last until the interpreter quits.
The statements executed by the top-level invocation of the interpreter, either read from a script file or interactively, are considered part of a module called __main__,
so they have their own global namespace. (The built-in names actually also live in a module; this is called __builtin__.)
'''

'''
Although scopes are determined statically, they are used dynamically. 
At any time during execution, there are at least three nested scopes whose namespaces are directly accessible:
the innermost scope, which is searched first, contains the local names
the scopes of any enclosing functions, which are searched starting with the nearest enclosing scope, contains non-local, but also non-global names
the next-to-last scope contains the current module’s global names
the outermost scope (searched last) is the namespace containing built-in names
'''

'''
Data attributes override method attributes with the same name; 
to avoid accidental name conflicts, which may cause hard-to-find bugs in large programs, 
it is wise to use some kind of convention that minimizes the chance of conflicts.
'''

'''
classes are not usable to implement pure abstract data types.
In fact, nothing in Python makes it possible to enforce data hiding.
'''

class SimpleAnimal:
    pass

print dir(SimpleAnimal)
#output: ['__doc__', '__module__']

class Animal(object):
    """
    This is class docstring
    """
    def __init__(self):
        print("Animal init called!")
        self.walk() # works well. method call in init
        # Try except works well in init
        try:
            self.walk()
        except:
            print("Unknown exception")

    def run(self):
        #walk()
        #NameError: global name 'walk' is not defined
        self.walk() #works well
        Animal.walk(self) #works well
    
    def print_docstring(self):
        print Animal.__doc__
        # Prints Animal Docstring
        print __doc__
        # Prints Module docstring

    def eat():
        print("eat called!")

    def walk(self):
        print("Animal walking!")


print dir(Animal)
'''
Output: (The difference is this class is inherited by object class)
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__modu
le__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook_
_', '__weakref__']
'''

#object creation:
a = Animal()
print dir(a)
'''
Same output as above
'''

a.run()
#Animal.eat()
# TypeError: unbound method eat() must be called with Animal instance as first argument (got nothing instead)
print a.run
# <bound method Animal.run of <__main__.Animal object at 0x7fdcdac7a410>>