is_sublist = lambda sub, main: all(item in main for item in sub)

list1 = [2, 3]
list2 = [1, 2, 3, 4, 5]

print(is_sublist(list1, list2))