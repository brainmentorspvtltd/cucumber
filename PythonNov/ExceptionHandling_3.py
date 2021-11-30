try:
    file = open('file_1.txt', 'w')
    data = "hello"
    file.write(data)
    data = file.read()
except FileNotFoundError:
    print("File was not found...")
finally:
    print("File Closed...")
    file.close()