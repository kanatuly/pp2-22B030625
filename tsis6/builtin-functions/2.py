s = input()

print(sum(x.islower() for x in s))
print(sum(x.isupper() for x in s))
