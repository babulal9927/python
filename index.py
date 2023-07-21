def two_sum(nums, target):
    num_index = {}  # Dictionary to store each number's index in the list

    # Iterate through the list and store each number's index in the dictionary
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_index:
            return [num_index[complement], i]
        num_index[num] = i

    return None  # If no solution is found

# Example usage:
nums = [3, 3]
target = 6
result = two_sum(nums, target)
print(result)  # Output: [0, 1]
