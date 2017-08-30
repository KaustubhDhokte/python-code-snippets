# -*- coding: utf-8 -*-
'''
When a derived class defines _ _init_ _() , the _ _init_ _() methods of base classes are
not automatically invoked.Therefore, it’s up to a derived class to perform the proper
initialization of the base classes by calling their _ _init_ _() methods. In the previous
example, this is shown in the statement that calls Account._ _init_ _() . If a base class
does not define _ _init_ _() , this step can be omitted. If you don’t know whether the
base class defines _ _init_ _() , it is always safe to call it without any arguments because
there is always a default implementation that simply does nothing.
'''

class Animal(object):
    def __init__(self):
        print("Animal init!")
    def run(self):
        print("Animal running!")
    def walk(self):
        print("Animal walking!")

class Dog(Animal):
    def __init__(self):
        print("Dog init\n")
        super(Dog, self).__init__()

    def run(self):
        print("Dog running!\n")


d = Dog()
#Dog init

#Animal init!

a = Animal()
# Animal init!
a.run()
# Animal Running!
d.run()
# Dog Running!
d.walk()
# Animal Walking!