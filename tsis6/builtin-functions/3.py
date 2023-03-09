def is_palindrome(s):
    return list(reversed(s)) == list(s)


print(is_palindrome("qazaq"))
print(is_palindrome("kazakh"))