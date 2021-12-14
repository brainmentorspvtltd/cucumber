# Logic
import read_write

class Employee:
    def __init__(self, name, dept, salary):
        self.__id = 101
        self.__name = name
        self.__dept = dept
        self.__salary = salary

    def __str__(self):
        return str(self.__id) + "," + self.__name + "," + self.__dept + "," + str(self.__salary)

def registerEmp(name, dept, salary):
    emp = Employee(name, dept, salary)
    print(emp)
    read_write.writeEmp(emp)