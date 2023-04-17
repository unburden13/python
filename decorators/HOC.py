# Higher Order Functions
# - functions that receive/return another function
# e.g. filter(), reduce()

def greet(func):
    func()


def greet2():
    def func():
        return 5
    return func

