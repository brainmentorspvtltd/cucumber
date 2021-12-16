import csv

def readEmp():
    data = []
    with open('employees.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def writeEmp(emp):
    with open('employees.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(str(emp).split(","))
