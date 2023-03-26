

'''
Generator is used for handling memory issue
'''


y = 1000_000_000
x = [i**2 for i in range(100)] 
# this above line can be improved

for el in x:
    print(el)


for i in range(100):
    print(i**2)
# this simply solves the problem but not the best way to solve