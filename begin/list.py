
# a = []
# # mylist = ['banana', 'cherry', 'lemon']
# # num = [2,4,6,0, -1, -4]
#
# # print(len(mylist))
# # mylist.append("vaazha")
# # # item = mylist.pop()
# # # item = mylist.sort()
#
# # newlist = sorted(num)
# # print(newlist)
#
# #@slicing
# # mylist = [1,2,4,5,6,7,8,9]
# # # a = mylist[:5]
# # a = mylist[1::5]
# # print(a)
#
# #     @ copying list
# mylist = ['banana', 'apple', 'cherry']
# # list_copy = mylist.copy()
# list_copy = mylist[:]
# list_copy.append("orange")
# print(list_copy)
# print(mylist)
#



# # @list comprehension
# # mylist = [1,2,3,4,5,6]
# # b = [i*i for i in mylist]
# # print(mylist)
# # print(b)
#
#
## For list of integers
# lst1 = []
#
# # For list of strings/chars
# lst2 = []
#
# lst1 = [int(item) for item in input("enter the value").split()]
# lst2 = [item for item in input("enter the item").split()]
#
#
# print(lst1)
# print(lst2)
#
#
#


# inp = int(input("enter number of item"))
# mylist = []
# for i in range(0, inp):
#     el = int(input())
#     mylist.append(el)
# print(mylist)


# lst = []
# n = int(input("Enter number of elements : "))
#
# for i in range(0, n):
#     ele = [input(), int(input())]
#     lst.append(ele)
#
# print(lst)

lst = []
item = [item for item in input("enter you value").split()]
print(item)