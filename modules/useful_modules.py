from collections import Counter, defaultdict, OrderedDict
import datetime
from array import array


# Counter: returns a Counter object with all items in an iterable and an occurrence counter for each of them
li = [1,2,3,4,4,4,5,6,7]
text = 'some random text'
print(f'Counter --> {Counter(li)}')
print(f'Counter --> {Counter(text)}')


# defaultdict: define a default value when accessing a non-existing item in a dictionary
dictionary = defaultdict(lambda: 5, {'a': 1, 'b': 2})
print(f'defaultdict --> {dictionary["c"]}')


# OrderedDict: Keeps the order of insertion in a dictionary.
# could have some performance implications.
# since python 3.7 dictionaries are ordered by default
d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d['b'] = 2  # this would make the difference
d['a'] = 1
print(f'OrderedDict --> {d == d2}')

d3 = {'c': 10}
d3['a'] = 1
d3['b'] = 2

d4 = {'c': 10}
d4['b'] = 2  # for regular dicts (before python 3.7) this would not make a difference
d4['a'] = 1
print(f'OrderedDict --> {d3 == d4}')


#datetime
print(f'datetime --> {datetime.time(5,31,18)}')  # creates a datetime object
print(f'datetime --> {datetime.date.today()}')


# array
# lists on python are dynamic (size and types) by default, meaning a lot of resources could be consumed
# arrays define the size and type on declaration so memory can be better used
# could be an alternative for generators
# https://docs.python.org/3/library/array.html
arr = array('i', [1,2,3])
print(f'array --> {arr}')
print(f'array --> {arr[0]}')

