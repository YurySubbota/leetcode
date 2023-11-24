roman = 'MCMXCIV'


def roman_to_integer(roman):
    value_of_symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer = 0
    integer_list = [value_of_symbols[i] for i in roman.upper()]
    i = len(integer_list)
    while i > 0:
        i -= 1
        try:
            if integer_list[i + 1] > integer_list[i]:
                integer += integer_list[i + 1] - integer_list[i]
                integer_list.pop()
                integer_list.pop()
            else:
                integer += integer_list[i + 1]
                integer_list.pop()
        except IndexError:
            ...
        if i == 0:
            integer += integer_list[i]
            integer_list.pop()
    return integer


print(roman_to_integer(roman))
