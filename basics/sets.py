#  unordered collection of unique objects

my_set = {1, 2, 3, 4, 5, 5} #  duplicate items will not be in the actual set
my_set.add(20)
print(my_set)

my_list = [1, 2, 3, 4, 5, 5]
print(set(my_list)) #  set() converts to a set
print(list(my_set)) #  list() converts to a list
print(3 in my_set) #  can't do my_set[0] since sets don't support indexing, you have to look for the item itself

your_set = {4, 5, 7, 8, 9}

#  common methods:
my_set.difference(your_set) #  tells the difference
my_set.difference_update(your_set) #  removes de difference
my_set.discard(5) #  removes the given item
my_set.intersection(your_set) #  tells the commont items -shortcut: my_set & your_set
my_set.isdisjoint(your_set) #  True if the two sets have nothing in common
my_set.union(your_set) #  unites the two sets together -shortcut: my_set | your_set
my_set.issubset(your_set) #  True if the entirety of my_set is inside your_set
my_set.issuperset(your_set) #  True if my_set encompasses the entirety of your_set
