# Suppose I want to implement this class


class Building(object):
     def __init__(self, floors):
         self._floors = [None]*floors
     def occupy(self, floor_number, data):
          self._floors[floor_number] = data
     def get_floor_data(self, floor_number):
          return self._floors[floor_number]

building1 = Building(4) # Construct a building with 4 floors
building1.occupy(0, 'Reception')
building1.occupy(1, 'ABC Corp')
building1.occupy(2, 'DEF Inc')
print( building1.get_floor_data(2) )


## This can be implemented with
class NewBuilding(object):
     def __init__(self, floors):
         self._floors = [None]*floors
     def __setitem__(self, floor_number, data):
          self._floors[floor_number] = data
     def __getitem__(self, floor_number):
          return self._floors[floor_number]

building1 = NewBuilding(4) # Construct a building with 4 floors
building1[0] = 'Reception'
building1[1] = 'ABC Corp'
building1[2] = 'DEF Inc'
print( building1[2] )


# The [] syntax for getting item by key or index is just syntax sugar.
# When you evaluate a[i] Python calls a.__getitem__(i) (or type(a).__getitem__(a, i)