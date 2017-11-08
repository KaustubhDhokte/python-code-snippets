class Base1(object):
    """
    """
    def dup_method(self):
        print "Base1 Dup method"
    
    def dup_method2(self):
        print "Base1 dup method 2"


class Base2(object):
    """
    """
    def dup_method(self):
        print "Base2 dup method"

    def dup_method2(self):
        print "Base2 dup method 2"


class Derived1(Base1, Base2):
    """
    """
    def dup_method(self):
        print "Derived1 dup method"


class Derived2(Base2, Base1):
    """
    """
    pass

d = Derived1()
d.dup_method2()

d = Derived2()
d.dup_method2()


#############################################################################################################

class First(object):
    pass

class Second(object):
    pass

class Third(First, Second):
    pass

print Third.mro()
# Output: [<class '__main__.Third'>, <class '__main__.First'>, <class '__main__.Second'>, <type 'object'>]
