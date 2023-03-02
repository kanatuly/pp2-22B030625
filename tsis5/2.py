import re

pattern = r'a[b]{2,3}'

print(re.match(pattern, "abba"))
print(re.match(pattern, "abbblkasd"))
print(re.match(pattern, "ab"))