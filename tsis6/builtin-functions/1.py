import itertools

s = list(map(int, input().split()))

print(list(itertools.accumulate(s, lambda x, y : x*y)).pop())

