haystack = 'sadbutsad'
needle = 'sad'


def find_the_index_of_the_first_occurrence_in_a_string(string1, string2):
    for i in range(len(string1)):
        if string2 in string1[i:len(string2)+i]:
            return i
    return -1


print(find_the_index_of_the_first_occurrence_in_a_string(haystack, needle))
