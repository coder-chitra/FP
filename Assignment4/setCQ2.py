def combination_sum(nums, target):

    result = []

    def backtrack(start, path, total):

        if total == target:
            result.append(path[:])
            return

        if total > target:
            return

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path, total + nums[i])
            path.pop()

    backtrack(0, [], 0)

    return result


numbers = [2, 3, 5, 7]

target = 10

print("Combinations:")
print(combination_sum(numbers, target))