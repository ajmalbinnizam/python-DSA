#
# #@  MULTI  THREADING ;; a thread is separate flow of execution
#                                        ///programm will have two  things happening once
#
# from threading import *
# from time import sleep
#
# class hi(Thread):
#     def run(self):
#         for i in range(3):
#             print("hi")
#             sleep(1)
#
# class helo(Thread):
#     def run(self):
#         for i in range(3):
#             print("hello")
#             sleep(1)
#
# t1=hi()
# t2=helo()
#
# t1.start()
# sleep(0.2)
# t2.start()
#
# t1.join()
# t2.join()
# print("bye")

#######@@@@ File handling ###@@@

# f=open('oops.py','r') #@@@ open a file and "r" is read
# # print(f.readline())
# # f=open('file','w')
#
# # f1=open('ab','w') # w is write
# f1=open('ab','a') #a is append
# f1.write('something')
# for data in f:
#     f1.write(data)

f=open('aju.jpg','rb') ## read in binary
f1=open('mypic.jpg','wb') ## write in binary of a new file mypic
for data in f:
    f1.write(data)



