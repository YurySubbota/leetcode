nums = [1, 3, 5, 6]
target = 4


def search_position(nums, target):
    for i in range(len(nums)):
        if nums[i - 1] < target < nums[i] and i != 0 or target == nums[i] or i == 0 and target < nums[i]:
            return i
        elif target > nums[len(nums) - 1]:
            return len(nums)


print(search_position(nums, target))
