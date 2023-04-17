from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2 - t1} s')

    return wrapper


"""
- much more performant when calculating large sets of data
- mostly for long loops where we don't want to store that memory and we don't have to calculate all at the same time
- a lot of libraries in python use generators under the hood
"""


@performance
def long_time():
    print('1')
    for i in range(100000000):
        i * 5


@performance
def long_time2():
    print('2')
    for i in list(range(100000000)):
        i * 5


long_time()
long_time2()
