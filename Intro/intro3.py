def func(x):
    if x == 1:
        def rv():
            print("X is eg to 1")
    else:
        def rv():
            print("X is not 1")
    return rv

new_func = func(2)
new_func() # X is not 1 

print(id(new_func)) # Address/memmory location of this fn 
 