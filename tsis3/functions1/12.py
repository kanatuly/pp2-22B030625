def histogram(arr):
    for x in arr:
        print('*' * x)


histogram(list(map(int, input().split())))