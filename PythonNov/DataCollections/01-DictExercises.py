data = {
    "names" : ["John","Sam","Mac","Tom","Nick"],
    "dept" : ["IT","HR","IT","IT","HR"],
    "salary" : [45000,38000,50000,65000,25000]
}

# 1. Get the salary of any specific emp
name = input("Enter Emp Name : ")
if name in data["names"]:
    index = data["names"].index(name)
    sal = data["salary"][index]
    print(f"Salary of {name} is {sal}")
else:
    print("Employee Not Found...")

# 2. Get the employees who works in IT Department

print("Employees who work in IT Department")
for i in range(len(data["names"])):
    if data["dept"][i] == "IT":
        name = data["names"][i]
        sal = data["salary"][i]
        print(f"Name : {name}, Salary : {sal}")

# 3. Get the average salary of those employees who works in HR dept
sum = 0
for i in range(len(data["names"])):
    if data["dept"][i] == "HR":
        sal = data["salary"][i]
        sum += sal

avgSal = sum / data["dept"].count("HR")
print("Average salary for HR Dept is :",avgSal)

# 4. Total salary paid to IT Department
sum = 0
for i in range(len(data["names"])):
    if data["dept"][i] == "IT":
        sal = data["salary"][i]
        sum += sal
print("Total salary for IT Dept is :",sum)