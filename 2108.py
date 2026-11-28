def read_strings():
    count = int(input("Enter number of strings in the array: "))
    strings = []
    for position in range(1, count + 1):
        strings.append(input("Enter the string at position " + str(position) + " : "))
    return strings


def is_palindrome(word):
    return word == word[::-1]


def first_palindrome(words):
    for word in words:
        if is_palindrome(word):
            return word
    return ""


print(first_palindrome(read_strings()))