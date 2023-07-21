def two_sum(nums, target):
    num_indices = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            return [num_indices[complement], index]
        num_indices[num] = index
    
nums = [3, 2, 4]
target = 6
output = two_sum(nums, target)
print(output)  # Output: [1, 2]
