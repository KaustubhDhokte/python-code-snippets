# https://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python
'''
A metaclass is the class of a class.
Like a class defines how an instance of the class behaves, a metaclass defines how a class behaves.
A class is an instance of a metaclass.
'''

'''
When the class statement is executed, 
Python first executes the body of the class statement as a normal block of code. 
The resulting namespace (a dict) holds the attributes of the class-to-be.
The metaclass is determined by looking at the baseclasses of the class-to-be (metaclasses are inherited), 
at the __metaclass__ attribute of the class-to-be (if any) or the __metaclass__ global variable. 
The metaclass is then called with the name, bases and attributes of the class to instantiate it.
'''
'''
>>> class MyShinyClass(object):
...       pass
can be created manually this way:

>>> MyShinyClass = type('MyShinyClass', (), {}) # returns a class object
>>> print(MyShinyClass)
<class '__main__.MyShinyClass'>
>>> print(MyShinyClass()) # create an instance with the class
<__main__.MyShinyClass object at 0x8997cec>

You'll notice that we use "MyShinyClass" as the name of the class and as the variable to hold the class reference. They can be different, but there is no reason to complicate things.

type accepts a dictionary to define the attributes of the class. So:

>>> class Foo(object):
...       bar = True
Can be translated to:

>>> Foo = type('Foo', (), {'bar':True})
And used as a normal class:

>>> print(Foo)
<class '__main__.Foo'>
>>> print(Foo.bar)
True
>>> f = Foo()
>>> print(f)
<__main__.Foo object at 0x8a9b84c>
>>> print(f.bar)
True
And of course, you can inherit from it, so:

>>>   class FooChild(Foo):
...         pass
would be:

>>> FooChild = type('FooChild', (Foo,), {})
>>> print(FooChild)
<class '__main__.FooChild'>
>>> print(FooChild.bar) # bar is inherited from Foo
True
Eventually you'll want to add methods to your class. Just define a function with the proper signature and assign it as an attribute.

>>> def echo_bar(self):
...       print(self.bar)
... 
>>> FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})
>>> hasattr(Foo, 'echo_bar')
False
>>> hasattr(FooChild, 'echo_bar')
True
>>> my_foo = FooChild()
>>> my_foo.echo_bar()
True
And you can add even more methods after you dynamically create the class, just like adding methods to a normally created class object.

>>> def echo_bar_more(self):
...       print('yet another method')
... 
>>> FooChild.echo_bar_more = echo_bar_more
>>> hasattr(FooChild, 'echo_bar_more')
True
You see where we are going: in Python, classes are objects, and you can create a class on the fly, dynamically.

This is what Python does when you use the keyword class, and it does so by using a metaclass.

'''