# Scope -> what variables do i have access to?
# scope order:
# 1 - start with local
# 2 - parent local
# 3 - global
# 4 - built-in python functions

# global keyword is used to access variables in the global scope
total = 0
def count():
    global total
    total += 1
    return total

count()
count()
print(count())

# global can be confusing as the file gets larger
# alternative approach would be:
total2 = 0
def count(total2):
    total2 += 1
    return total2

print(count(count(count(total2))))


# nonlocal keyword is used to refer to the parent local scope
def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)

outer()