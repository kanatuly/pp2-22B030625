import re

pattern = r'(?=[A-Z])'

print(re.split(pattern, "AaskdmaAAlksaddaAass"))
