class Test():
    def __init__(self,age):
        self.age=age
    def __getattribute__(self,attribute):
        print("Initializing getattribute")
        return 6
    def __setattr__(self,attribute,value):
        print("Initializing setattr")
        return object.__setattr__(self,attribute,value)
test=Test(4)
test.age
print(test.age)

#output
# Initializing setattr
# Initializing getattribute
# Initializing getattribute
# 6

# if I comment line 9 return object.__setattr__(self,attribute,value)
# Nothing changes.
 # explaination
#  __getattribute__ is called before any other attempt is made to access an
# attribute. No matter what __setattr__ does, test.age is handled by 
# test.__getattribute__("age"), which returns 6 whether or not there
# is an attribute named age


# If you get rid of __getattribute__:
class Test():
    def __init__(self,age):
        self.age=age
    def __setattr__(self,attribute,value):
        print("Initializing setattr")
        return object.__setattr__(self,attribute,value)

test=Test(4)
test.age
print(test.age)

# Output
# 4


# If you further get rid of the call to object.__setattr__
class Test():
    def __init__(self,age):
        self.age=age
    def __setattr__(self,attribute,value):
        print("Initializing setattr")

test=Test(4)
test.age
print(test.age)

# Output
# Initializing setattr
# Traceback (most recent call last):
#   File "/Users/chepner/tmp.py", line 11, in <module>
#     test.age
# AttributeError: 'Test' object has no attribute 'age'

# Explaination
# then you'll get an AttributeError because self.age = age will never actually 
# create or set the age attribute; 
# it just prints the initialization message and returns:
# go to test.py file