# trying to understand getattr and getattribute dunder methods

# A key difference between __getattr__ and __getattribute__ is that
# __getattr__ is only invoked if the attribute wasn't found the usual ways.


# __getattribute__ is called whenever an attribute access occurs.


class Foo(object):
    def __init__(self, a):
        self.a = 1

    ## correct way
    def __getattribute__(self, attr):
        return super().__getattribute__(attr)
    
    ## wrong way
    def __getattribute__(self, attr):
        try:
            return self.__dict__[attr]
        except KeyError:
            return 'default'
f = Foo(1)
# f.a  -->  this will create infinite loop

# This will cause infinite recursion. The culprit here is the line return self.__dict__[attr]. 
# Let's pretend (It's close enough to the truth) that all attributes are stored in self.__dict__ and available
# by their name. The line
#           f.a
# attempts to access the a attribute of f.
# This calls f.__getattribute__('a').__getattribute__ then 
# tries to load self.__dict__. __dict__ is an attribute of
# self == f and so python calls
#     f.__getattribute__('__dict__') 
# which again tries to access the attribute '__dict__'. This is infinite recursion.

# correct way explaination
# super().__getattribute__(attr) binds the __getattribute__ method of the 'nearest' superclass
# (formally, the next class in the class's Method Resolution Order, or MRO) to the 
#  current object self and then calls it and lets that do the work.

# All of this trouble is avoided by using __getattr__ which lets Python 
# do it's normal thing until an attribute isn't found. 
# At that point, Python hands control over to your __getattr__ method and lets it come up with something.

# If __getattr__ had been used instead then

# 1. It never would have run because f has an a attribute.
# 2. If it had run, (let's say that you asked for f.b) then it would not have been called
#   to find __dict__ because it's already there and __getattr__ is invoked only 
#   if all other methods of finding the attribute have failed.





# It's also worth noting that you can run into infinite recursion with __getattr__.

class Foo(object):
    def __getattr__(self, attr):
        return self.attr # --> infinte loop as attr not there it will keep calling itself
    

# Using the __getattr__ magic method, we can intercept that 
# inexistent attribute lookup and do something so it doesn’t fail:

class Dummy(object):

    def __getattr__(self, attr):
        return attr.upper()

d = Dummy()
d.does_not_exist # 'DOES_NOT_EXIST'
d.what_about_this_one  # 'WHAT_ABOUT_THIS_ONE'

# But if the attribute does exist, __getattr__ won’t be invoked:

class Dummy(object):

    def __getattr__(self, attr):
        return attr.upper()

d = Dummy()
d.value = "Python"
print(d.value)  # "Python"

# __getattribute__ is similar to __getattr__, with the important 
# difference that __getattribute__ will intercept EVERY attribute lookup,
#  doesn’t matter if the attribute exists or not.

class Dummy(object):

    def __getattribute__(self, attr):
        return 'YOU SEE ME?'

d = Dummy()
d.value = "Python"
print(d.value)  # "YOU SEE ME?"

