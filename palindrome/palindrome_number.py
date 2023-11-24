number = 1234567890987654321


def palindrome(number):
    i = len(str(number))
    backwards = ''
    while i > 0:
        i -= 1
        backwards += str(number)[i]
    if str(number) == backwards:
        return True
    return False


def palindrome2(number):
    backwards = str(number)[::-1]
    if str(number) == backwards:
        return True
    return False


print(palindrome(number))
print(palindrome2(number))
