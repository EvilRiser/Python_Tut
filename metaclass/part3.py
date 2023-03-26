# if we add type/ inherit from type then it becomes metaclass
class Meta(type):
    def __new__(self,class_name,bases,attrs):
        '''
        calls before init
        '''
        print(attrs)

        # later added
        a = {}
        for key,value in attrs.items():
            if key.startswith("__"):
                a[key] = value
            else:
                a[key.upper()] = value 
        print(a)
        return type(class_name,bases,a)


class Dog(metaclass=Meta):
    x=5
    y=8
    def hello(self):
        print("Hi")

# If we run now then
# {'__module__': '__main__', '__qualname__': 'Dog', 'x': 5, 'y': 8, 'hello': <function Dog.hello at 0x7f5f80872ee0>}
# {'__module__': '__main__', '__qualname__': 'Dog', 'X': 5, 'Y': 8, 'HELLO': <function Dog.hello at 0x7fc36f704ee0>}


d = Dog()
print(d.X) # 5