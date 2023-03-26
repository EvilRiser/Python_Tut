'''
Class view for generator
'''

class Gen:
    def __init__(self,n):
        self.n = n
        self.last = 0


    def __next__(self):
        return self.next()
    
    def next(self):
        if self.last == self.n:
            raise StopIteration()
        rv = self.last ** 2
        self.last += 1
        return rv


g = Gen(100)

while True:
    try:
        print(next(g))  # --> this next calls __next__ method
    except StopIteration:
        break


'''
Here we are not keeping track of the list
but just the last state of the number

'''