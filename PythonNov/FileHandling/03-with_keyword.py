import easygui

# file = open('file_1.txt')
# data = file.read()
# print(data)
# file.close()

path = easygui.fileopenbox()
print(path)

with open(path) as file:
    data = file.read()
    print(data)
