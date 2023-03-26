from queue import Queue as q
import inspect


class Queue(q):
    def __repr__(self):
        return f"Queue({self._qsize()})"
    def __add__(self,item):
        self.put(item)
    def __sub__(self,item):
        self.get()

qu = Queue()
print(qu) # Queue(0)

# print(inspect.getsource(Queue))
qu + 9
print(qu)

qu + 7
qu + 6

qu - 0
print(qu)
qu - None
print(qu)