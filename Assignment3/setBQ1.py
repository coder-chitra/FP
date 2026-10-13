def check_type(value):

    if isinstance(value, int):
        print("Integer detected")
        print("Square =", value * value)

    elif isinstance(value, str):
        print("String detected")
        print("Length =", len(value))

    elif isinstance(value, list):
        print("List detected")
        print("Number of elements =", len(value))

    else:
        print("Unsupported type")

check_type(10)
check_type("Functional Programming")
check_type([1, 2, 3, 4])