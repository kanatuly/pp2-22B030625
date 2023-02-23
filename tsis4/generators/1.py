def square_numbers(n):
    i = 0
    while i <= n:
        yield i*i
        i += 1


for x in (x*x for x in range(33)):
    print(x)