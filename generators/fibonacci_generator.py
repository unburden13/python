# F_n = F_n-1  +  F_n-2 -- general formula
# F_0 = 0,  F_1 = 1 -- initial values

def fib(number):
    index_1 = 1
    index_2 = 0
    for i in range(number):
        yield index_2  # meaning, nothing will be saved in memory, just the last value
        temp = index_2
        index_2 = index_1
        index_1 = temp + index_1

for n in fib(20):
    print(n)  # take each result one by one and act upon it, in this case, printing it


def fib_using_list(number):
    index_1 = 1
    index_2 = 0
    result = []
    for i in range(number):
        result.append(index_2)  # meaning, everything will be saved in memory
        temp = index_2
        index_2 = index_1
        index_1 = temp + index_1
    return result

print(fib_using_list(20))