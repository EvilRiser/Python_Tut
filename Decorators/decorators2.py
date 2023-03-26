def func(f):
    def wrapper():
        print("Started")
        f()
        print("Ended")
    return wrapper


def func2():
    print(
        "I am func2"
    )


x = func(func2)
print(x)
x()
# <function func.<locals>.wrapper at 0x7f33a70c7ee0>
# Started
# I am func2
# Ended

def func3():
    print("I am func3")

x = func(func3)
print(x)
x()
# <function func.<locals>.wrapper at 0x7f127bc8a040>
# Started
# I am func3
# Ended

func3 = func(func3)
func3()
# Started
# I am func3
# Ended


'''
Here our main method is func2 or func3 but we want extra computations to
be added so we are passing our main func (func3/func2) in our 
helping method `func`

Whenever we want to make decorator use the wrapper class concept
def func(f): --> it takes the main fn as parameter
    def wrapper(x,y): --> it takes the arg of main fn
        do whatever you want
        f()

    return wrapper
        


func3 = func(func3)
Instead of writing this use
@func
def func3():
    ...
'''

@func
def func4():
    print("I am func4")

func4()
