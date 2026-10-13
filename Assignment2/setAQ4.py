def square(x):
    return x * x

def double(x):
    return x * 2

def compose(f, g, x):
    return f(g(x))

result = compose(square, double, 3)

print("Result =", result)