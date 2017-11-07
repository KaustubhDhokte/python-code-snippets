# https://www.toptal.com/python/interview-questions

def extendList(val, lst=[]):
    lst.append(val)
    return lst

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print "list1 = %s" % list1
print "list2 = %s" % list2
print "list3 = %s" % list3

'''
Output:
list1 = [10, 'a']
list2 = [123]
list3 = [10, 'a']
'''

'''
However, what actually happens is that the new default list is created only once when the function is defined, 
and that same list is then used subsequently whenever extendList is invoked without a list argument being specified.
This is because expressions in default arguments are calculated when the function is defined, not when it’s called.
list1 and list3 are therefore operating on the same default list, whereas list2 is operating on a separate list that it created (by passing its own empty list as the value for the list parameter).
The definition of the extendList function could be modified as follows, though, to always begin a new list when no list argument is specified, which is more likely to have been the desired behavior:
def extendList(val, list=None):
  if list is None:
    list = []
  list.append(val)
  return list
With this revised implementation, the output would be:
list1 = [10]
list2 = [123]
list3 = ['a']
'''


