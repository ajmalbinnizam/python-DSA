#lambda arg : expression

# ad10 = lambda x: x+10
# print(ad10(5))
# def ad10fun(x):
#     return x+10
#
# mult = lambda x,y:x*y
# print(mult(2,7))
#
# point2d = [(1,2),(15,1),(5,-1)]
# point2dsorted = sorted(point2d, key=lambda x:x[0] + x[1])
#
# print(point2dsorted)

#------------map(fun, seq)
a = [1,2,3,4,5]
b = map(lambda x: x+2, a)
print(list(b))

c= [x*2 for x in a]
print(c)


#------filter(func, seq)
a = [1,2,3,4,5]
b = filter(lambda x: x%2==0, a)
print(list(b))

c = [x for x in a if x%2==0]
print(c)


#-----Reduce(fun, seq)
from functools import reduce
a = [1,2,3,4,5,6]
product_a = reduce(lambda x,y: x*y, a)
print(product_a)
c = [x for x in a ]
print(a)