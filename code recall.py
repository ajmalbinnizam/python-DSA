# a=[1,2,3,4]
# # b=a.append(8)
# # print(a)

# val=[1,2,2]
# sum=0
# for num in val:
#     sum=sum+num
#     sub=num-sum
# print("is total number",sum)
# print("is total sub number",sub)
# print(list(range(10)))

# genre=['pop','metal','rob']
# for i in range(len(genre)):
#     print(genre[i])
#     break;

#     #mATRIX MULTIPLICATION
# from array import *
#
# a=[[2,7,3],
#    [4,5,6],
#    [7,8,9]]
# b=[[5,8,1],
#    [6,7,3],
#    [4,5,9]]
# result=[[0,0,0],
#         [0,0,0],
#         [0,0,0]]
#
# for i in range(len(a)):#iterarting row of a
#     for j in range(len(b)):#iterating col of b
#         for k in range(len(b)):
#             result[i][j]+=a[i][k]*b[k][j]
# for r in result:
#     print(r)
#
lst=[]
n=int(input('enter the size of element'))
for i in range(0,n):
    ele= int(input('enter val'))
    lst.append(ele)
for num in lst :
    if num%2==0:
        print(num,end=" ")

