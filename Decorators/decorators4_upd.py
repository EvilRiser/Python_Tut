def my_decorator(my_func):
    def wrapper(*args, **kwargs):
        print("In the decorator")
        ret_fn = my_func(*args, **kwargs)
        print("Ending decorator")
        return ret_fn
    return wrapper


@my_decorator
def my_func1(x, y):
    print("Inside my func1")
    print(x)
    return y

@my_decorator
def my_func2():
    print("my func 2 with no arg")


y = my_func1(10,20)
print(y)

my_func2()