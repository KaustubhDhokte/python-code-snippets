# https://www.python-course.eu/sets_frozensets.php
'''
Though sets can't contain mutable objects, sets are mutable: 
>>> cities = set(["Frankfurt", "Basel","Freiburg"])
>>> cities.add("Strasbourg")
>>> cities
set(['Freiburg', 'Basel', 'Frankfurt', 'Strasbourg'])
>>> 

Frozensets are like sets except that they cannot be changed, i.e. they are immutable:
>>> cities = frozenset(["Frankfurt", "Basel","Freiburg"])
>>> cities.add("Strasbourg")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'frozenset' object has no attribute 'add'
>>> 
'''