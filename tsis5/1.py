import re

pattern = r'a[b]*'

print(re.match(pattern, "abba"))
print(re.match(pattern, "alkasd"))
print(re.match(pattern, "a"))