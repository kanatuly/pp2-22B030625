import re

pattern = r'[A-Z][a-z]+'
matches = re.findall(pattern, "Aasda1asdaAAAsaasADa")

for match in matches:
    print(match)
