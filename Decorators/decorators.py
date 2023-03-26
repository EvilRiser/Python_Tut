def func(string):
    def wrapper():
        print("Started")
        print(string)
        print("Ended")
    # return wrapper() # We return wrapper being called so just instantiating func class will print all above
    return wrapper # In this case we have to call the object of func class as well x()


x = func("Hello")
# Started
# Hello
# Ended

x()