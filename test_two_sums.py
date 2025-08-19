"""
Two Sum (Hash Map approach)
Given an array and a target, return the indices of two numbers that add up to the target.
"""

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]
        seen[num] = i


print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))