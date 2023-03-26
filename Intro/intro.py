def make_class(x):
    class Dog:
        def __init__(self,name):
            self.name = name
        
        def print_value(self):
            print(x)
    
    return Dog   # Here we are passing reference to the class not actually the instance of class(Dog())


cls = make_class(10)

print(cls) # <class '__main__.make_class.<locals>.Dog'> 

# Here main comes from name of our module(__main__)
# make_class is the function we have created
# locals is the whats inside of the fn
# and dog tells us the actual name of the class

d = cls("SSS") # --> creating instance of class 
d.print_value() # 10
# Since cls is now a class so we will use it how we use a class
print(d.name) # SSS

