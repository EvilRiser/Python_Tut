def gen(n):
    for i in range(n):
        yield i**2
        # rather than stopping the iteratrion at return yield just pauses it
        # we have all the information on this function i,n we have not returned anything just paused it

g = gen(100)

# for i in g:
#     print(i)

print(next(g))
print(next(g))

for _ in range(100):
    print(next(g)) 
    # problem with this an above is it will raise stopiteration exception
    # but above one will not

