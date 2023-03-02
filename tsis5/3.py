import re

pattern = r'[a-z]+_[a-z]+'
matches = re.findall(pattern, 'a_sadas_dasAasda_asa___asdaqw2123_1')

for match in matches:
    print(match)