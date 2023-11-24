strs = ['flower', 'flow', 'flight']


def longest_common_prefix(list1):
    prefix = list1[0]
    for string in list1:
        temp_string = ''
        ind = 0
        for i in prefix:
            try:
                if i == string[ind]:
                    temp_string += i
                ind += 1
            except IndexError:
                ...
        prefix = temp_string
    return f'"{prefix}"'


print(longest_common_prefix(strs))
