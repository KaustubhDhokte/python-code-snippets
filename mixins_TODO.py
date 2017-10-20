'''
the mixin classes weren't made to stand on their own.
In more traditional multiple inheritance, the AuthenticationMixin (for example) would probably be 
something more like Authenticator. 
That is, the class would probably be designed to stand on its own.
'''

'''
The basic idea of a mixin is to create a small re-usable class that can "plug-in" to other larger classes.
From the wikipedia definition, a mixin is a way to compose classes together without using inheritance.
The problem is unlike ruby, python mixins are a purely conceptual construct.
Python mixins are inheritance (the only difference is that the class name usually contains 'Mixin').
It is up to the developer to remember this, and to manually avoid all of the common pitfalls of multiple inheritance.
This kind of defeats the whole purpose of the mixin in the first place.
What's more is that most people use python mixins improperly.
'''

'''
from book import Book
from index import IndexMixin

class TextBook(Book, IndexMixin):
    def __init__(self, name, contents, edition='1st'):
        Book.__init__(self, name, contents)
        self.edition = edition

t = TextBook('Learn Python the Hard Way')
t.search('python')
>>> 0 results found

'''