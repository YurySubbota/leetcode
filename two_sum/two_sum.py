nums = [2, 2, 7, 11, 15]
target = 18


def two_sum(target, nums):
    for first in range(len(nums)):
        for second in range(first + 1, len(nums)):
            if nums[first] + nums[second] == target:
                return first, second


print(two_sum(target, nums))
