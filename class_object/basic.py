# What is the difference between __init__, __call__ and __new__

# __init__()
# __init__() method in the python constructor is invoked automatically when 
# an object of the class is defined. It can also be invoked with the values provided 
# during the time of declaration of the object of the class.

class A: 
     def __init__(self, number): 
         print("__init__() call") 
         self.data = number
     def __str__(self):
         print("__str__() call")
         print("Number is {}".format(self.data))

# Class A declaration
x = A(16) 
x.__str__()

# Declaration of another instance
y = A(20)
y.__str__()

## Output
# __init__() call
# __str__() call
# Number is 16
# __init__() call
# __str__() call
# Number is 20


# __call__()


class A:
    def __init__(self, number):
        print("__init__() call")
        self.data = number
    def __str__(self):
        print("__str__() call")
        print("Number is {}".format(self.data))
    def __call__(self):
       num = 0
       print("__call__() call")
       print("Adding 10 to the value of data")
       num = self.data + 10
       return num

x = A(16)
x.__str__()
y = x()
print(y)

# Declaration of another instance of class A

z = A(23)
z.__str__()

# __call__() calling for z

return_val = z()
print(return_val)

## Output
# __init__() call
# __str__() call
# Number is 16
# __call__() call
# Adding 10 to the value of data
# 26
# __init__() call
# __str__() call
# Number is 23
# __call__() call
# Adding 10 to the value of data
# 33



# __new__()
# __new__ method will be called when an object is created. __init__ method will
# be called to initialize the object. __new__ method is defined as a static 
# method that requires passing a parameter argument1.
class Devnote(object):
    def __str__(self):
        return "Devnote"

class Dev(object):
    def __new__(argument1):
	    return Devnote()
    def __init__(self):
	    print ("init call")

print(Dev())
## Output
# Devnote

class A(object):
    def __new__(cls):
         print("Creating instance")
         return super(A, cls).__new__(cls)
  
    def __init__(self):
        print("Init is called")
  
A()
## Output
# Creating instance
# Init is called

# The above example shows that __new__ method is called automatically when 
# calling the class name, whereas __init__ method is called every time an instance
#  of the class is returned by __new__ method, passing the returned 
#  instance to __init__ as the self parameter

# This means that if the super is omitted for __new__ method 
# the __init__ method will not be executed.

class A(object):
    def __new__(cls):
        print("Creating instance")
  
    # It is not called
    def __init__(self):
        print("Init is called")
  
print(A())

## Output
# Creating instance
# None



# EXample

"""
x = A(16) # statement 1
x() # statement 2
y = B() # statement 3
y() # statement 4

__init__() is called statement 1
__call__() is called statement 2
__new__() is called statement 4
"""


