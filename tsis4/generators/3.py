def multiples34(n):
    i = 0
    while i < n:
        if i % 3 == 0 or i % 4 == 0:
            yield i
        i += 1


n = int(input())
for x in multiples34(n):
    print(x, end = ' ')
print()
for x in (x for x in range(n) if x % 3 == 0 or x % 4 == 0):
    print(x, end = ' ')