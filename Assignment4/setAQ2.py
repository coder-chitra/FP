def triangular_numbers(n):
    return [i * (i + 1) // 2 for i in range(1, n + 1)]

def apply_function(func, sequence):
    return list(map(func, sequence))

def square(x):
    return x * x

nums = triangular_numbers(5)

print("Triangular Numbers:", nums)
print("Squared Values:", apply_function(square, nums))