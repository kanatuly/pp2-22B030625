import os

path = "../builtin-functions/1.py"

if not os.access(path, os.F_OK):
    print("does not exist")
else:
    print("directory: " + os.path.dirname(path))
    print("name: " + os.path.basename(path))