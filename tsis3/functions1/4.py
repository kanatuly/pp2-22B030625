def is_prime(n):
    if n < 2:
        return False
    x = 2
    while x*x <= n:
        if n % x == 0:
            return False
        x += 1
    return True


def filter_primes(numbers):
    primes = []
    for number in numbers:
        if (is_prime(number)):
            primes.append(number)
    return primes


numbers = list(map(int, input().split()))
print(filter_primes(numbers))