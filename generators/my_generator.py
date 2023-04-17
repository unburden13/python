def my_generator(num):
    for i in range(num):
        yield i * 2  # yield pauses the function and comes back to it when calling the 'next' keyword

g = my_generator(10)

print(next(g))
print(next(g))
print(next(g))
