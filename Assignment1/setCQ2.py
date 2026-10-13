def compose(f):
    def outer(g):
        def inner(x):
            return f(g(x))
        return inner
    return outer

def square(x):
    return x * x

def double(x):
    return x * 2

result = compose(square)(double)

print(result(5))