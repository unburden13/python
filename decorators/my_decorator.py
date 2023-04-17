def my_decorator(func):
    """simple decorator"""
    def wrap_func():
        print('==========')
        func()
        print('==========')
    return wrap_func


def my_decorator_2(func):
    """with dynamic params"""
    def wrap_func(*args, **kwargs):
        print('----------')
        func(*args, **kwargs)
        print('----------')
    return wrap_func


@my_decorator
def hello():
    print('heey')

@my_decorator_2
def bye(text, name, emoji=':)'):
    print(text, name, emoji)

hello()
bye('so long,', 'alex', ':(')