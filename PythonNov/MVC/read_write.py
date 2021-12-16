import csv

def readEmp():
    pass

def writeEmp(emp):
    with open('employees.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(str(emp).split(","))
