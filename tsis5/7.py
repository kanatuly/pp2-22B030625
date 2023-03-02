import re

pattern = r'_([a-z])'

print(re.sub(pattern, lambda x: x.group(1).upper(), "_astq_sadads_Asaw"))
