def is_prime(x):
    if x < 2: return False
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            return False
    return True


arr = list(map(int, input().split()))
arr = list(filter(lambda x: is_prime(x), arr))
print(arr)