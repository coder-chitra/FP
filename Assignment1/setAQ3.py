def square():
    def inner(x):
        return x * x
    return inner

sq = square()
num = int(input("Enter number: "))
print("Square =", sq(num))