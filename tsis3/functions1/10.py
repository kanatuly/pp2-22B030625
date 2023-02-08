def uniquify(arr):
    return list(dict.fromkeys(arr).keys())


print(uniquify(list(map(int, input().split()))))