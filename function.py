# def add(x,y):
#     c=x+y
#     d=x-y
#     return c,d
#
# result1,rslt2=add(2,4)
# print(result1,rslt2)
# a=10
# b=20
# def add(a,b):
#     result=a+b #local variable
#     print("addittion",result)
#     return
# add(a,b) #global variable
# print("add outside",result) #local variable

# def add():
#     a=int(input("enter the number"))
#     b=int(input("enter the number"))
#     result=a+b
#     print("add",result)
#
# add()

# def add(a,b):
#     result=a+b
#     return result
# result=add(9,5)
# print(result)
#
# name =input(("enter ur name"))
# age=int(input(" enter ur age"))
# def printme(name,age):
#     print("my name",name)
#     print("my age",age)
#     return
# printme(name="aju",age=22)
#
# def welcome(*names):
#     for pearu in names:
#         print("hi",pearu)
# welcome("aju","jech")
# call by value ,PARA WILL BE COIPED AND NO VALUE CHANGE
# cALL BY ReferenceE,THE ADDRESS OF THE PARAMETER COPIED,VALUES ARE CHANGED
# def add(l):
#       l.append(5)
#       print(id(l),l)
#
# mylist=[1,2,3]
# print(id(mylist),mylist)
# add(mylist)
# def update(x):
#     print(id(x),"x",x)
#     x[1]=6
#     print(id(x),"x aft update",x)
# a=[1,2,3]
# print(id(a),"a",a)
# update(a)

# TYPES OF ARGUMENT
# FORMAL ARGUMENT:fn il ulla arg or paramter
# ACTUAL ARGUMENT: def cheyna fn ull arg>>keyword (name,age), default(age =18),variable lenghth(*b)


# POSITIONAL ARGUMENT
# def sum(*b): #variable length multiple values
#     c=0
#     for i in b:
#         c=i+c
#     print(c)
# sum(1,2,3)

##@@@@@@@@@@@@@@##### keywordARGvariableLENGTH ###@@@@@@@@@@@@@@############

# def person(name ,**age):
#     print(name)
#     print(age)
#     for i,j in age.items():
#         print(i,j)
# person('ajmal',age=22,num=81299)

# GLOBAL AND LOCAL VARIABLE
# a=10
# print(id(a),a,'org a')
# def num():
#     global a
#     a = 6
#     print(a,'global')
#     x=globals()['a']
#     print(id(x),x)
#     print('in fun',a)
#     globals()['a']=17
# num()
# print('out',a)

# PASS LIST TO A FUNCTION
# def count(lst):
#     even=0
#     odd=0
#     for i in lst:
#         if i%2==0:
#             even+=1
#         else:
#             odd+=1
#     return even,odd
# lst=[2,3,7,8,2,9,7]
# evn,odd=count(lst)
# print(odd,'odd number')
# print(evn,'even number')
# print("evn :{} and odd :{}".format(evn,odd))
#

# ########@@@@@@@@@@@@@   FIBONACCI ############@@@@@@@@@@
def fib():
    n=int(input('enter ur series'))
    a=0
    b=1
    if n<0:
        print("invalid")
    elif n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            if c>=n:
                break;
            print(c)

fib()

# #@@@#####@@@@@@@@@@@@@@@@@ FACTORIAL@@@@@@@@@@###############
# def fac(n):
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#     return f
# print(fac(5))

#  RECURSION
# import sys
# sys.setrecursionlimit(100)
# print(sys.getrecursionlimit())
# i=0
# def greet():
#     global i
#     i+=1
#     print('hello',i)
#     greet()
# greet()
# FACT RECURSION
# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)
# x=int(input('enter the number'))
# result=fact(x)
# print(result,'is your factorial')
#ANONYMOUS FUNCTION
# FUN      FUN  ARG
# f=lambda a,b:a+b
# res=f(5,3)
# resu=f(6,3)
# print(res)
# print(resu)

# # FILTER
# # def even(n):
# #     return n%2==0
# num=[2,3,5,8,5,2,6,9,5,3]
# # filtereven=list(filter(even,num))
# filtereven=list(filter(lambda n:n%2==0,num))
# # MAP oru list inta akat ad or un cheyan
# # def doub(n):
# #     return n*2
# # mapdoubles=list(map(doub,filtereven))
# mapdoubles=list(map(lambda n:n*2,filtereven))
# print(mapdoubles)
# #REDUCE
# from functools import reduce
# # def sum(a,b):
# #     return a+b
# # reduce=reduce(sum,mapdoubles)
# reduce=reduce(lambda x,y:x+y,mapdoubles)
# print(reduce)

# #DECORATOR
# def div(a,b):
#     print(a/b)
#
# def smartdiv(func):
#     def inner(a,b):
#         if a<b:
#             a,b=b,a
#             return func(a,b)
#     return inner
# div=smartdiv(div)
# div(2,4)
