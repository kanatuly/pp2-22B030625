def even_numbers(n):
    i = 0
    while i <= n:
        yield i
        i += 2



n = int(input())
range(0, n+1, 2)

for x in even_numbers(n):
    print(x)