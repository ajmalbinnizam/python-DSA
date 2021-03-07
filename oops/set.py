#set is in built datatype in python which is unoredered and mutable and no duplicates

myset = set('helo')
print(myset)


setA = {1,2,3,4,5,6}
setB = {1,2,3}
setC = {8,9}
print(setA.issuperset(setB))
print(setA.isdisjoint(setB))
