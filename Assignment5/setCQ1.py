from itertools import islice

def fibonacci():
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()

print(list(islice(fib, 10)))