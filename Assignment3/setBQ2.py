def first_item(lst):
    return lst[0] if lst else None

print(first_item([100, 200, 300]))
print(first_item(["A", "B", "C"]))
print(first_item([True, False]))