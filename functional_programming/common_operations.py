from functools import reduce

my_list = [1,2,3,4,5,6]
your_list = [10,20,30,40,50,60]
their_list = [12,11,10,9,8]

def multiply_by_3(item):
    return item * 3

print(f'map: {list(map(multiply_by_3, my_list))}')  # returns a new list --> doesn't produce any side effect


def only_odds(item):
    return item % 2 != 0

print(f'filter: {list(filter(only_odds, my_list))}')


print(f'zip: {list(zip(my_list, your_list, their_list))}')


def accumulator(acc, item):
    return acc + item

print(f'reduce: {reduce(accumulator, my_list, 0)}')

