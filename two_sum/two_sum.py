nums = [2, 7, 11, 15]
target = 17
def two_sum(target, nums):
    a = 0
    b = 0
    for first in nums:

        for second in nums:
            if first + second == target:
                print(first, second, target)
                return [a, b]
            b += 1
        a += 1

print(two_sum(target, nums))