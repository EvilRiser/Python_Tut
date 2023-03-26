class Person:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return f"Person({self.name})"
    def __mul__(self,x):
        '''
        When some int is multiplied with object of this class
        '''
        if type(x) is not int:
            raise Exception("Invalid argument must be int")
        self.name = self.name*x
    def __call__(self, y):
        '''
        If we put brackets() in an object or call an object then this method is called
        Example:
        p = Person("some_name")
        p(4) --> at this point this method is called
        '''
        print("called this function",y)
    def __len__(self):
        '''
        When we try to use len on some object this method is called
        '''
        return len(self.name)

p = Person("SS")
print(p)  # Prints the memory address location
# after adding repr we can see the output as Person(SS)


p*4
print(p) # Person(SSSSSSSS)

p(4) # -->  called this function 4
print(len(p)) # 8