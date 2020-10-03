def f(x, y=None):

    if y == None:
        return x**2
    else:
        return x**2 + y**2
print(f(1))
print(f(1,2))

