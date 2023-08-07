class Test():
    def __init__(self,age):
        self.age=age  # Invoking setattr
    def __getattribute__(self,attribute):
        print("Initializing getattribute")
        return 6
    def __setattr__(self,attribute,value):
        print("Initializing setattr")
        # return object.__setattr__(self,attribute,value)
test=Test(4)
test.age # Invoking getattribute
print(test.age) # invoking getattribute

class Test2():
    def __init__(self,age):
        self.age=age
    def __setattr__(self,attribute,value):
        print("Initializing setattr")

test2=Test2(4) # invokes set attr
test2.age  # --> this is creating error
# print(test2.age) # --> this is creating error