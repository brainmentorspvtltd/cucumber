# def even(num):
#     return num % 2 == 0
#
# def odd(num):
#     return num % 2 != 0

# print(even(6))
numbers = [4,4,6,8,93,45,7,8,11,4,3,67,8,23,7,8,4]

# ev = list(filter(even, numbers))
# print(ev)

ev = list(filter(lambda n : n % 2 == 0, numbers))
print(ev)
