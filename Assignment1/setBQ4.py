def power(x):
    def inner(y):
        return x ** y
    return inner

square = power(2)
cube = power(3)

print("2^5 =", square(5))
print("3^4 =", cube(4))