# x = 5
# if x < 0:
#     raise Exception("x should be postive")
# # x = -5
# # assert (x>=0), "x is not positive"
# try:
#     a = 5/0
# except Exception as e:
#     print(e)
#     print('an error happened')

# try:
#     a = 5 / 0
#     b = a + 4
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else:
#     print('fine!')
# finally:
#     print('cleaning up')

class ValueTooHighError(Exception):
    pass