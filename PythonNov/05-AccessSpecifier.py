class Employee:

    def __init__(self, id, name, dept, salary):
        self.__id = id
        self.__name = name
        self.__dept = dept
        self.__salary = salary
        # self.salary = salary
        print("Param Const...")

    def show(self):
        print(self.__id, self.__name, self.__dept, self.__salary)
        print(self.salary)
        # print("Hello")

ram = Employee(101, 'Ram', 'IT', 45000)
ram.salary = 10000
ram.show()

shyam = Employee(102, 'Shyam', 'HR', 56000)
shyam.salary = 30000
shyam.show()
