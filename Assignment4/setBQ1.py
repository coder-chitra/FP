def get_string_lists(data):

    return list(filter(lambda x: isinstance(x, str), data))

items = [10, "Python", 20, "Java", True, "C++"]

print(get_string_lists(items))