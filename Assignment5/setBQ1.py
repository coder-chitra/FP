from itertools import combinations

elements = input("Enter elements separated by space: ").split()

print("All Combinations:")

for r in range(1, len(elements) + 1):
    for combo in combinations(elements, r):
        print(combo)