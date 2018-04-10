def f(x):
    x = x + 1
    print('in f(x): x =', x)
    return x
x = 3 #global scope binding
z = f(x)
