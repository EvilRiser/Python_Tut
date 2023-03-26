class Foo:
    def show(self):
        print("hi")

def add_attribute(self):
    self.z = 9


Test = type('Test',(Foo,),{"x":5,"add_attribute":add_attribute})

t = Test()
t.wy = "Hello"
print(t.wy) # "Hello"
print(t.x) # 5
t.show() # hi
print(t.show()) # None

t.add_attribute()
print(t.z )
