def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculator(operation, x, y):
    return operation(x, y)

print("Addition =", calculator(add, 10, 5))
print("Subtraction =", calculator(subtract, 10, 5))
print("Multiplication =", calculator(multiply, 10, 5))
print("Division =", calculator(divide, 10, 5))