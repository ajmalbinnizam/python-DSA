from array import *
# val = array('i',[-5,7,8,2,6])
# vals=array('u',['a','b','c','d'])
# newarr = val
# val.reverse()
# print(val.buffer_info())
# print(val.typecode)
# for i in range (5):
#     print(val[i])
# for e in newarr:
#     print(e)
# print(sorted(val))

#user defined array
# arr=array('i',[])
# num=int(input('enter the no of val'))
# for i in range(num):
#     x=int(input('enter ur vale '))
#     arr.append(x)
# print(arr)
# #
# val=int(input('enter num to search'))
# k=0
# for e in arr:
#     if e==val:
#         print(k)
#         break
#     k+=1
# print(arr.index(val))
# from numpy import*
# arr=array([4,5,5,8.0],float)
# print(arr.dtype)
# print(arr)
# from array import *
# arr=array('i',[1,2,3,4])
# arr=linspace(0,9,10)
# arr=arange(1,10,2)
# arr=logspace(1,40,5)
# arr=ones(3,int)
# print(arr)
# print('%.2f'%arr[2])
# from numpy import*
# arr1=array([9,2,3,5],int)
# arr2=array([1,2,3,5],int)
# arr=arr1+arr2
# print(sorted(arr))
# print(concatenate([arr1,arr2]))
from array import *
# a=array('i',[1,2,3,4])
# b=array('i',[1,2,3,4])
# c=array('i',[])
# for i in range(0,4):
#     c.append(a[i]+b[i])
# print(c)
from numpy import*
# ar=array([5,8,3,4])
# ar.sort()
# print(ar)
# print(ar[len(ar)-1],'is the max')
# martix
# from numpy import *
# m1=matrix('1 1;1 1')
# m2=matrix('2 2;2 3')
# m3=m1*m2
# print(m3)

a=array([[1,2],
         [3,4]])
b=array([[2,4],
         [6,8]])
c=a*b

print(len(a))
