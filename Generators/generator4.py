def gen():
    yield 10
    yield 100
    yield 1000
    yield 10000

g = gen()

print(next(g))
print(next(g))
