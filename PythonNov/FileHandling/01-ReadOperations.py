file = open('file_1.txt')
# data = file.read()

# file.seek(25)
# data = file.read(20)

# data = file.readline(2)

data = file.readlines()
file.close()

print(data)