def my_decorator(my_func):
    def wrapper(x):
        print("In the decorator")
        my_func(x)
        print("Ending decorator")
    return wrapper


@my_decorator
def my_func1(x):
    print("Inside my func1")
    print(x)


@my_decorator
def my_func2():
    print("my func 2 with no arg")


my_func1(10)
# In the decorator
# Inside my func1
# 10
# Ending decorator

# but what if we do the same for my_func2
my_func2()
# Traceback (most recent call last):
#   File "decorators3.py", line 27, in <module>
#     my_func2()
# TypeError: wrapper() missing 1 required positional argument: 'x'

'''
To fix this error we use unpack operator in wrapper func
    def wrapper(*args,**kwargs): --> accept all arg and key word arguments
        print("In the decorator")
        my_func(*args,**kwargs)
        print("Ending decorator")
    return wrapper


'''


