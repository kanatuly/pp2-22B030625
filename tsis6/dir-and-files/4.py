file = open("4.py", 'r')

lines = 0

for _ in file:
    lines += 1

print(lines)

file.close()