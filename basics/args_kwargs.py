#  *args : tuple
#  **kwargs : dictionary
#  Rule: params, *args, default params, **kwargs
#  example: some_sum(name, *args, age=10, **kwargs)

def some_sum(*args, **kwargs):
    print(args)
    print(kwargs)

    total = 0
    for item in kwargs.values():
        total += item

    return sum(args) + total


print(some_sum(1,2,3,4,5, num1=1, num2=2))

