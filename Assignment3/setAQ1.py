def first_element(lst):
    if len(lst) == 0:
        return None
    return lst[0]

print(first_element([10, 20, 30]))
print(first_element(["Python", "Java", "C++"]))
print(first_element([True, False]))