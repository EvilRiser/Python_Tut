# Descriptor Protocol

# descr.__get__(self, obj, type=None) --> value
# descr.__set__(self, obj, value) --> None
# descr.__delete__(self, obj) --> None

# If an object defines both __get__() and __set__(), it is
# considered a data descriptor. Descriptors that only
# define __get__() are called non-data descriptors (they are typically used
#  for methods but other uses are possible).


# Data and non-data descriptors differ in how overrides are calculated with respect
# to entries in an instance’s dictionary. If an instance’s dictionary has an
# entry with the same name as a data descriptor, the data descriptor takes precedence.
#  If an instance’s dictionary has an entry with the same name as a non-data descriptor,
#  the dictionary entry takes precedence.

# To make a read-only data descriptor, define both __get__() and __set__() with
# the __set__() raising an AttributeError when called. Defining the __set__()
# method with an exception raising placeholder is enough to make it a data descriptor.


# A descriptor can be called directly by its method name. For example, d.__get__(obj).
# Alternatively, it is more common for a descriptor to be invoked automatically upon 
# attribute access.


# The important points to remember are:

#  * descriptors are invoked by the __getattribute__() method
#  * overriding __getattribute__() prevents automatic descriptor calls
#  * object.__getattribute__() and type.__getattribute__() make different 
#         calls to __get__().
#  * data descriptors always override instance dictionaries.
#  * non-data descriptors may be overridden by instance dictionaries.


