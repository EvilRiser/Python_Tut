'''
shared memory and spaces
locking and unlocking
problem with open and not close state beacuse of some error
'''

file = open("file.txt","w")
file.write("hello")
file.close()

file = open("file.txt","r")
try:
    file.write("yeahh")
finally:
    file.close()

# equivalent to
with open("file.txt","r") as file:
    file.write("NOOO")