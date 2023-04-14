#  tuples are immutable -unlike lists

my_tuple = (1, 2, 3, 4, 5, 5)
x = my_tuple[0]
y = my_tuple[2:4]
print(x)
print(y)
print(my_tuple.count(5))
print(my_tuple.index(2))
print(len(my_tuple))

item = my_tuple[3]
list = [1]
list.append(item)
print(list)