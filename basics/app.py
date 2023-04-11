from math import *
import this


def average(operands):
    sum_result = sum(operands)
    count = len(operands)
    avg = sum_result / count
    return avg


def get_even_numbers(operands):
    even_numbers_list = []
    for number in operands:
        if number % 2 == 0:
            even_numbers_list.append(number)
    return even_numbers_list


numbers_list = []

first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
third_number = float(input("Enter third number: "))
show_even = input("Show even numbers? y/n: ")

# list methods to add:
#     append: adds to the end
#     insert: adds to a given index
#     extend: adds another list
# list methods to remove:
#     pop: removes last index
#     remove: removes the first item of a given value
#     clear: clears the whole list
# list methods to search:
#     in: 'x' in list  -- returns true or false
#     sort: list.sort() -- returns nothing, modifies the list
#     sorted: sorted(list) -- returns sorted list without modifying the initial list
#     reverse: basket.reverse()
#     count: list.count('a') returns the number of times the specified element appears in the list
#
# list[{start}:{end}:{step}]
# list[::-1] -- reverses the list
# list(range(100)) -- creates a list with numbers from 1 to 100
# '-'.join(['hey','how','are','you']) --joins items in the given list using the initial string. Result: hey-how-are-you
#
# list unpacking
# (1) a,b,c = [1,2,3] -- a -> 1, b -> 2, c -> 3
# (2) a,b,c,*other = [1,2,3,4,5,6] -- (1) *other -> [4,5,6] -as a list
# (3) a,b,c,*other,d = [1,2,3,4,5,6,7] -- (1)(2) d -> 7
#
#



numbers_list.append(first_number)
numbers_list.append(second_number)
numbers_list.append(third_number)

result_string = "Result: " + str(average(numbers_list)) + ". "

if show_even == "y":
    even_numbers = get_even_numbers(numbers_list)
    result_string += "Even numbers: " + str(even_numbers)
elif show_even == "n":
    result_string += "Even numbers calculation omitted"
else:
    result_string += "No even numbers or omitted calculation."

print(result_string)




