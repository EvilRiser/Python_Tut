def my_decorator(my_func):
    def wrapper(*args, **kwargs):
        print("In the decorator")
        my_func(*args, **kwargs)
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
my_func2()
# In the decorator
# my func 2 with no arg
# Ending decorator