def combine(a, b):

    if isinstance(a, int) and isinstance(b, int):
        return a + b

    elif isinstance(a, str) and isinstance(b, str):
        return a + b

    elif isinstance(a, list) and isinstance(b, list):
        return a + b

    else:
        raise TypeError("Unsupported types")

print(combine(10, 20))
print(combine("Hello ", "World"))
print(combine([1, 2], [3, 4]))