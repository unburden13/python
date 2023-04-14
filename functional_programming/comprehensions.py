# list, set, dictionary

my_list = [char for char in 'python']
my_list2 = [num for num in range(0,100)]
my_list3 = [num ** 2 for num in range(0,100)]
my_list4 = [num ** 2 for num in range(0,100) if num % 2 == 0]


my_set = {char for char in 'pythonnn'}  # same as lists, but with brackets {}


simple_dict = {
    'a': 1,
    'b': 2
}

my_dict = {key: value**2 for key, value in simple_dict.items()}  # same as sets, but look at the variables
my_dict2 = {key: value**2 for key, value in simple_dict.items() if value % 2 == 0}
my_dict3 = {num: num*2 for num in [1,2,3]}  # setting the key name

some_list = ['a','b','c','b','d','m','n','n']
duplicates = list({item for item in some_list if some_list.count(item) > 1})
print(duplicates)
