import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"Started function {func.__name__}")
        val = func(*args, **kwargs)
        total = time.time() - start
        print("Time:",total)
        print(f"Ended function {func.__name__}")
        return val
    return wrapper


@timer
def test():
    for _ in range(1000):
        pass

@timer
def test2():
    time.sleep(2)

test()
test2()

'''
Some more examples of decorator could be the logging decorator
or arg validation
'''