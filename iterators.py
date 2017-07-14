i = iter([1, 2, 3])
print i
print i.next()

j = iter({1:'a', 2:'b'})
print j.next()
print j.next()
#print j.next()

k = iter((6, 7, 8))
print k.next()
print k.next()
print k.next()
print k.next()
# StopIteration
