from collections import Counter as counter
a = 'aaaaaaaabbbccc'
my_counter = counter(a)
print(my_counter.values())
print(my_counter.most_common(1))
print(my_counter.most_common(1)[0][0])

print(list(my_counter.elements()))


from collections import namedtuple
point = namedtuple('Point', 'x,y')
pt = point(1, -4)
print(pt.x,pt.y)


from collections import OrderedDict

