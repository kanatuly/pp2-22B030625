def reverse(string):
    arr = string.split(' ')
    arr.reverse()
    return ' '.join(arr)


print(reverse(input()))