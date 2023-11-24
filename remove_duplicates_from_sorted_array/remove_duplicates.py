nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]


def remove_duplicates_from_sorted_array(numbers):
    numbers = list(set(numbers))
    return f'{len(numbers)}, nums = {numbers}'


print(remove_duplicates_from_sorted_array(nums))
