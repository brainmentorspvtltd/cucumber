# def add(*x):
#     # print(x)
#     if len(x) > 1:
#         sum = 0
#         for i in range(len(x)):
#             sum += x[i]
#         print("Sum is",sum)
#
# add(5,5)
# add(4,5,76)
# add(1,2,4,6,8,8,4)
# add(5)
# add()

# def details(name, age, sal, *address):
#     print(name)
#     print(age)
#     print(sal)
#     print(address)
#
# details("Ram", 45, 45600, "Delhi", "Chennai", "Pune")

# def person(**details):
#     print(details)
#
# person(name = "Ram", age=45)

def person(*args, **kwargs):
    print(args, kwargs)



