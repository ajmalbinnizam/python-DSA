# import calc
#
# x=8
# y=9
# c=calc.add(x,y)
# d=calc.sub(x,y)
# print(c)
# print(d)



# import calc
# print('demo says:'+ __name__)
# def aju():
#     print('hello')
#     print('melcow')
#
# if __name__ == "__main__":
#     aju()
#
# import calc
# def fun1():
#     c=calc.add() #<<<<
#     print('hoi from fun1')
# def fun2():
#     d=calc.sub()
#     print('vanakam from fun2')
# def main():
#     fun1()
#     fun2()
# main()


# ###########@  CLASS OOPS @@#########
# class computer: #1 classname
#     def __init__(self,cpu,ram): #constructor
#         # print('init in')
#         self.cpu=cpu #Assigning value to cpu
#         self.ram=ram
#
#     def config(self): #2 method
#         print('config is ', self.cpu,self.ram)
# com1 =computer('i5',16) #3 object
# com2=computer('ryzen5',8)
# # computer.config(com1)
# com1.config()
# com2.config()


#@@@@@@@ CONSTRUCTOR SELF COMPARING
# class computer:
#     pass
#     def __init__(self):
#         self.name = 'ajmal'
#         self.age = 22
#
#     def update(self):
#         self.name = 'ummj'
#         self.age = 32
#     def compare(self,other):
#         if self.age==other.age:
#             return True
#         else:
#             return False
# c1 = computer()
# # c1.age=30
# c1.update()
# c2 = computer()
# if c1.compare(c2):
#     print("they are same")
# else:
#     print("they are differnt")
# # c1.name = 'hazr'
# # c1.age = 23
# # print(c1.name)
# # c1.update()
# print(c1.name,c1.age)
# print(c2.name,c2.age)
# #

# @@@@@@@@#TYPES OF VARIABLE --INSTANCE ,CLASS(STATIC)
# class car:
#     wheel =4 #calss (static )variable
#     def __init__(self): ###instance variable
#         self.mil=10
#         self.com='bmw'
# c1=car()
# c2=car()
#
# car.wheel=5
#
# c1.mil=8
# print(c1.com,c1.mil,c1.wheel)
# print(c2.com,c2.mil,car.wheel)


# ######TYPES OF METHOD instance,class ,static@@@@@@@@@
# class student:
#     school= 'ajmal univ'
#     def __init__(self,m1,m2,m3):
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3
#     def avg(self):
#         return (self.m1+self.m2+self.m3)/3
#
#     @classmethod
#     def getschl(cls):
#         return cls.school
#     @staticmethod
#     def info():
#         print("this is static")
#
# s1=student(22,63,62)
# s2=student(54,23,76)
# print(s1.avg())
# print(student.getschl())
# student.info()

# #@@@@@@@@@@@ INNER CLASS@@@@@@@@@@
# class student: #outter class
#     def __init__(self,name ,rollno):
#         self.name=name
#         self.rollno=rollno
#         self.lap=self.laptop()
#
#     def show(self):
#         print(self.name,self.rollno)
#         self.lap.show()
#
#     class laptop: #inner class
#         def __init__(self):
#             self.brand='lenovo'
#             self.ram="8gb"
#         def show(self):
#             print(self.brand,self.ram)
# s1=student('aju',4)
# s2=student('alex',5)
# # # lap1=student.laptop()
# # s1.lap.brand
# s1.show()

# @@@@@@@@INHERITANCE@@@@@@@@@@@@@
# class a:
#     def __init__(self):
#         print('inint A constr')
#     def feature1(self):
#         print("feat 1")
#     def feature2(self):
#         print("feat 2")
# class b:
#     def __init__(self):
#         super().__init__()
#         print('inint B constr')
#     def feature3(self):
#         print("feat 3")
#
# class c(a,b):   #c(b):
#     def __init__(self):
#         print("inint c")
#         super(c, self).__init__()
#     def feature5(self):
#         print("feat 0")

# a1=a()
# b1=b()
# a1=c()
# a1.feature1()
# a1.feature2()
# b1.feature3()
# b1.feature4()
# c1.


# @@@@@@@@@@@@@@@@@@@@@POLYMORPHISM  @@@@@@@@@@@@@@@@@@@@@@@
###1 DUCK TYPING ###
# class pycharm:
#     def execute(self):
#         print('running')
#         print('compiling')
#
# class myide:
#     def execute(self):
#         print('convention check')
#         print('error debugging')
#         print('smooth running')
# #
# # class laptop:
# #
# #     def code(self,ide):
# #         ide.execute()
#
# ide=pycharm()
# ide=myide()
#
# # lap1=laptop()
# # lap1.code(ide)
# ide.execute()

### 2 operator overloading ###

# a=4
# b=4
# print(a+b)
# print(int.__add__(a,b))
#
# class students:
#     def __init__(self,m1,m2):
#         self.m1=m1
#         self.m2=m2
#
#     def __add__(self, other): #student.add(m1,m2)
#         m1=self.m1+other.m1
#         m2=self.m2+other.m2
#         s3=students(m1,m2)
#         return s3
#     # def __gt__(self, other):
#     #     r1=self.m1+self.m2
#     #     r2=other.m1+other.m2
#     #     if r1>r2:
#     #         return True
#     #     else:
#     #         return False
# s1=students(22,45)
# s2=students(23,64)
#
# s3= s1 + s2    #overloading
# print(s3.m2)
# # if s1>s2:
# #     print("s1 wins")
# # else:
# #     print('s2 wins')
# #

 #@@@@@@  3 method over loading  @@@@@@@@@@@

# class student:
#     def sum(self,a=None,b=None,c=None):  #@@@@method overloading
#         s=0
#         if a!=None and b!=None and c!=None:
#             s=a+b+c
#         elif a!=None and b!=None:
#             s=a+b
#         else:
#             s=a
#         return s
#
# s1=student()
# print(s1.sum(45))

###@@@@@@   4  method overriding   @@@#####
# class a:
#     def show(self):
#         print('a  show')
# class b(a):
#     def show(self):
#         print('b show')
#
#
# # b1=b() ####object
# a1=b()
# a1.show()
#

####@@@@@@ Iterator @@@####@@@@@@@@@@@@

# num=[5,4,6,3]
# it=iter(num)
# # print(it.__next__())
# # print(next(it))
# for i in it:
#     print(i)

#######specific value of ascend

# class top:
#     def __init__(self):
#         self.num=1
#
#     def __iter__(self):
#         return self
#     # def __next__(self):
#     #     if self.num<=10:
#     #         val=self.num
#     #         self.num+=1
#     #         return val
#     #     else:
#     #         raise StopIteration
#     def __next__(self):
#         if self.num <= 10:
#             val = self.num*self.num
#             self.num += 1
#             return val
#         else:
#             raise StopIteration
# values=top()
# # print(values.__next__())
# for i in values:
#     print(i)
#
###@@@@ generator###@@@
# def top():
#     n=1
#     while n<=10:
#         val=n*n
#         yield val #@@@ YIELD ADD OF VARI OR additionAL GENERATOR
#         n+=1
#
# val=top()
# for i in val:
#     print(i)


###@@@   ERROR handling  ###

# a=3
# b=0
#
# try:
#     print('resource open')
#     print(a/b)
#     print('resource open')
# except Exception as e:
#     print('exception==',e)
# finally:
#     print('resource close')