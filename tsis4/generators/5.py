def reversed_range(n):
    i = n
    while i >= 0:
        yield i
        i -= 1


t = reversed_range(10)
for x in t:
    print(x)