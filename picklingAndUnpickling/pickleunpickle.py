# -*- coding: utf-8 -*-

'''
The pickle module implements a fundamental, but powerful algorithm for serializing and de-serializing a Python object structure. 
“Pickling” is the process whereby a Python object hierarchy is converted into a byte stream, and “unpickling” is the inverse operation, whereby a byte stream is converted back into an object hierarchy.
Pickling (and unpickling) is alternatively known as “serialization”, “marshalling,” [1] or “flattening”, however, to avoid confusion, the terms used here are “pickling” and “unpickling”.
'''

'''
The cPickle module supports serialization and de-serialization of Python objects, providing an interface and functionality nearly identical to the pickle module. 
There are several differences, the most important being performance and subclassability.
First, cPickle can be up to 1000 times faster than pickle because the former is implemented in C.
Second, in the cPickle module the callables Pickler() and Unpickler() are functions, not classes. 
This means that you cannot use them to derive custom pickling and unpickling subclasses. 
Most applications have no need for this functionality and should benefit from the greatly improved performance of the cPickle module.
The pickle data stream produced by pickle and cPickle are identical, so it is possible to use pickle and cPickle interchangeably with existing pickles.
There are additional minor differences in API between cPickle and pickle, however for most applications, they are interchangeable.
More documentation is provided in the pickle module documentation, which includes a list of the documented differences.
'''

'''
marshal vs pickle

This module contains functions that can read and write Python values in a binary format. 
The format is specific to Python, but independent of machine architecture issues 
(e.g., you can write a Python value to a file on a PC, transport the file to a Sun, and read it back there). 
Details of the format are undocumented on purpose; it may change between Python versions (although it rarely does).
This is not a general “persistence” module.
For general persistence and transfer of Python objects through RPC calls, see the modules pickle and shelve.
The marshal module exists mainly to support reading and writing the “pseudo-compiled” code for Python modules of .pyc files.
Therefore, the Python maintainers reserve the right to modify the marshal format in backward incompatible ways should the need arise. 
If you’re serializing and de-serializing Python objects, use the pickle module instead – 
the performance is comparable, version independence is guaranteed, and pickle supports a substantially wider range of objects than marshal.
'''

'''
The pickle module differs from marshal in several significant ways:

The pickle module keeps track of the objects it has already serialized, 
so that later references to the same object won’t be serialized again. 
marshal doesn’t do this.

This has implications both for recursive objects and object sharing. 
Recursive objects are objects that contain references to themselves. 
These are not handled by marshal, and in fact, 
attempting to marshal recursive objects will crash your Python interpreter.
Object sharing happens when there are multiple references to the same object in 
different places in the object hierarchy being serialized. 
pickle stores such objects only once, and ensures that all other references point to the master copy. 
Shared objects remain shared, which can be very important for mutable objects.

marshal cannot be used to serialize user-defined classes and their instances. 
pickle can save and restore class instances transparently, however the class definition must be importable and live in the same module as when the object was stored.

The marshal serialization format is not guaranteed to be portable across Python versions. 
Because its primary job in life is to support .pyc files, the Python implementers reserve the right to change the serialization format in non-backwards compatible ways should the need arise.
The pickle serialization format is guaranteed to be backwards compatible across Python releases.

Note that serialization is a more primitive notion than persistence; although pickle reads and writes file objects, it does not handle the issue of naming persistent objects, nor the (even more complicated) issue of concurrent access to persistent objects.
The pickle module can transform a complex object into a byte stream and it can transform the byte stream into an object with the same internal structure. 
Perhaps the most obvious thing to do with these byte streams is to write them onto a file, but it is also conceivable to send them across a network or store them in a database. 
The module shelve provides a simple interface to pickle and unpickle objects on DBM-style database files.
'''
'''
Protocol version 0 is the original ASCII protocol and is backwards compatible with earlier versions of Python.
Protocol version 1 is the old binary format which is also compatible with earlier versions of Python.
Protocol version 2 was introduced in Python 2.3. It provides much more efficient pickling of new-style classes.
'''

'''
None, True, and False
integers, long integers, floating point numbers, complex numbers
normal and Unicode strings
tuples, lists, sets, and dictionaries containing only picklable objects
functions defined at the top level of a module
built-in functions defined at the top level of a module
classes that are defined at the top level of a module
instances of such classes whose __dict__ or the result of calling __getstate__() is picklable (see section The pickle protocol for details).
'''

import pickle
data = {'a':'b', 1:2, 3:'d'}

with open('pickled_data', 'w+') as f:
    pickle.dump(data, f)

with open('pickled_data', 'r+') as f:
    s = pickle.load(f)
    print s

data2 = [1, 2, 3, 4]

with open('pickled_data', 'w+') as f:
    p = pickle.Pickler(f)
    p.dump(data2)
    f.seek(0)
    up = pickle.Unpickler(f)
    print up.load()

# p.dump(data2)
# ValueError: I/O operation on closed file

