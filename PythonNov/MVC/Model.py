# Logic
import read_write

class Employee:
    def __init__(self, name, pwd, dept, salary):
        self.__id = 101
        self.__name = name
        self.__pwd = pwd
        self.__dept = dept
        self.__salary = salary

    def __str__(self):
        return str(self.__id) + "," + self.__name + "," + self.__pwd + "," + self.__dept + "," + str(self.__salary)

def registerEmp(name, pwd, dept, salary):
    emp = Employee(name, pwd, dept, salary)
    print(emp)
    read_write.writeEmp(emp)

def loginEmp(name, pwd):
    employees = read_write.readEmp()
    for i in range(len(employees)):
        if employees[i][1] == name and employees[i][2] == pwd:
            msg = ["Login Success", employees[i]]
            break
    else:
        msg = ["Invalid Id or Password",]
    return msg

