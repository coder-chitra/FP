def circumference(radius):
    return 2 * 3.14 * radius

def apply_function(func, value):
    return func(value)

r = float(input("Enter radius: "))
print("Circumference =", apply_function(circumference, r))