# https://stackoverflow.com/questions/111234/what-is-a-callable-in-python
class MyInt(int):
    def __call__(self, g=None):
        print "\nMyInt callable\n"
        if g is not None:
            print g

i = MyInt()

i() # MyInt callable

i(4)
'''
MyInt callable
4
'''