def next_permutation(p):
    i = len(p) - 2
    while i >= 0 and p[i] >= p[i+1]:
        i -= 1
    if i < 0:
        return False
    j = len(p) - 1
    while p[i] >= p[j]:
        j -= 1
    temp = p[i]
    p[i] = p[j]
    p[j] = temp
    p[i + 1:] = reversed(p[i + 1:])
    return True


s = list(input())
s = sorted(s)
print(''.join(s))
while next_permutation(s):
    print(''.join(s))
