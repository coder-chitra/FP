def square(x):
    return x * x

def add_ten(x):
    return x + 10

def compose(f, g):
    return lambda x: f(g(x))

result = compose(add_ten, square)

print("Result =", result(5))