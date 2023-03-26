# class defines rule for var and methods
# metaclass defines rules for class
def hello():
    class Hi:
        pass
    return Hi


class Test:
    pass

print(Test) # <class '__main__.Test'>
print(Test()) # <__main__.Test object at 0x7fb34f80e3d0>     

print(type(Test())) # <class '__main__.Test'>
print(type(2)) # <class 'int'>
print(type(hello)) # <class 'function'>
print(type(Test)) # <class 'type'>

# When we call this class we call type constructor using different things
# in our class to make this class object

MyTest = type('MyTest',(),{})
# this constructor creates a class on basis of 
        # name , bases(anything we inherit from), any attributes 
print(MyTest()) # <__main__.MyTest object at 0x7f815581f3d0>
print(MyTest) # <class '__main__.MyTest'>

class MyTest:
    pass

# this 2 things above are completely equivalent


