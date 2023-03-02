import re

pattern = r'(?<!^)(?=[A-Z])'

print(re.sub(pattern, '_', "AasdasAkajjkasKasas").lower())