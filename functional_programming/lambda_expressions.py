from functools import reduce
my_list = [1,2,3,4,5,6]

print(f'map using lambda: {list(map(lambda item: item * 4, my_list))}')

print(f'reduce using lambda: {reduce(lambda acc, item: acc + item, my_list)}')

another_list = [5,4,3]
print(f'square of items on list using lambda: {list(map(lambda item: item ** 2, another_list))}')

a = [(0,2),(4,3),(9,9),(10,-1)]
print(f'new list ordered by the second item on each tuple: {sorted(map(lambda item: item[1], a))}')
a.sort(key=lambda x: x[1])
print(f'sort the tuple list by the second item on each tuple: {a}')