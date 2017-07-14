# Problem 1: Write an iterator class reverse_iter, that takes a list and iterates it from the reverse direction.
# http://anandology.com/python-practice-book/iterators.html
class Reverse_Iter():
    def __init__(self, lst):
        self.lst = lst
        self.index = len(lst)-1

    def next(self):
        if self.index >= 0:
            ret = self.lst[self.index]
            self.index -= 1
            return ret
        raise StopIteration("Sampla ki bhava")

r = Reverse_Iter([1, 2, 3, 4])
while 1:
    print r.next()