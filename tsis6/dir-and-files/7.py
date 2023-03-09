file1 = open("A.txt", 'r')
file2 = open("B.txt", 'w')

file2.write(file1.read())

file1.close()
file2.close()