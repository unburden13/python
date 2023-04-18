def for_loop_under_the_hood(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator) * 2)
        except StopIteration:
            break

for_loop_under_the_hood([1,2,3])


class MyGen():  # mimic of 'range'
    current = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):  # allows to create an iterable - to iterate the object of the class
        return self

    def __next__(self):  # allows to use the next that 'for' runs under the hoods
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration  # 'for' automatically catches this ex. to stop looping

gen = MyGen(0, 100)
for i in gen:
    print(i)