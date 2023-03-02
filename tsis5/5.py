import re

pattern = r'a.*b$'

print(re.match(pattern, "abba"))
print(re.match(pattern, "abbblkasdb"))
