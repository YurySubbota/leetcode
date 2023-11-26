haystack = '1sadbutsad'
needle = 'sad'


def finde_the_index_of_the_first_occurrence_in_a_string(string1, string2):
    if string2 not in string1:
        return "not"
    for i in range(len(string1)):
        print(string1[i:len(string1)])
        print()
        if string2 in string1[i:len(string2)+i]:
            return i-1



print(finde_the_index_of_the_first_occurrence_in_a_string(haystack, needle))
#finde_the_index_of_the_first_occurrence_in_a_string(haystack, needle)