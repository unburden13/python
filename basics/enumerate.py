#  useful if you need an index counter of the iterable object

for i, char in enumerate("Heeey how are you"):
    print(i, char)

for i, num in enumerate(range(100)):
    if num == 50:
        print(f'index of 50 is {i}')
