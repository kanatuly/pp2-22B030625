def squares(a, b):
    i = a
    while i <= b:
        yield i*i
        i += 1


t = squares(4, 8)
for x in t:
    print(x)





