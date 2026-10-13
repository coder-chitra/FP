def add5(x):
    return x + 5

def double(x):
    return x * 2

def square(x):
    return x * x

def compose_three(f, g, h, x):
    return f(g(h(x)))

result = compose_three(square, double, add5, 3)

print("Result =", result)