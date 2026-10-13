def multiply(x):
    def inner(y):
        return x * y
    return inner

def square(x):
    return x * x

double = multiply(2)

result = square(double(5))

print("Result =", result)