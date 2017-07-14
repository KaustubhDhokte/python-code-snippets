# import learnimports Imports all succesffuly
from learnimports import *

# print _a  NameError _a not defined with wild card import
print e_
# print __d   NameError __d not defined with wild card import
# print __c__ NameError __c__ not defined with wild card import

'''
print learnimports._a
print learnimports.e_
print learnimports.__d
print learnimports.__c__
'''
class B(object):
    def __init__(self):
        pass

    def _single(self):
        print("Single UScore")

    def __double(self):
        print("Double UScore")

    def leading_single_(self):
        print("Leading Single")
    
    def __leadingAndTrailingDouble__(self):
        print("Leading and trailing Double")

class D(B):
    def __init__(self):
        pass

    def test(self):
        self._single()
        #self.__double()    throws AttributeError
        self._B__double()
        self.leading_single_()
        self.__leadingAndTrailingDouble__()

d = D
print(type(d))
d = D()
print(type(d))

d.test()