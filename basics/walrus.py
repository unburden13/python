# walrus operator ( := ) assigns values to variables as part of a larger expression
a = 'heeeeeeeeeey'
if (n := len(a)) > 10:
    print(f"too long {n} elements")

