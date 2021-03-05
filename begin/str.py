# my_string = "   helio world"
# my_string1 = my_string[1::3]
# print(my_string1)
#
# print(my_string.upper())
# print(my_string.count('o'))
# print(my_string.replace('helio', 'hello'))
# my_split = my_string.strip()
# print(my_split)
#
# my_spli = "how,are,you"
# my_spl= my_spli.split(',')
# print(my_spl)
# new_string = ''.join(my_spl)
# print(new_string)
# #------------------
# from timeit import default_timer as timer
# my_list = ['a'] * 1000000
# print(my_list)
#
#  #bad
# start = timer()
# new_str = ''
# for i in my_list:
#     new_str +=i
# print(new_str)
# stop = timer()
# print(stop-start)
#
#
#
#    #good
# start = timer()
# new_str = ''.join(my_list)
# print(new_str)
# stop = timer()
# print(stop - start)



#----------fstrings______
var = 3.1234
var1 = 6
print(f'variable value is {var*2} and {var1}')