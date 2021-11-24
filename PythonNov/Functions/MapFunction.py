# def temp_convert(c):
#     return 9/5 * c + 32
#
# def km_to_m(km):
#     return km * 1000
#
# def m_to_km(m):
#     return m / 1000

temp = [33.4,23.56,34.7,21.45,38.7,31.3]
kms = [4,6,8,4,5,8,9]
ms = [3434,67,89,2323,6789,9934]

# def myMap(func, iter):
#     data = []
#     for i in range(len(iter)):
#         data.append(func(iter[i]))
#     return data
#
# f = myMap(temp_convert, temp)
# print(f)
#
# mts = myMap(km_to_m, kms)
# print(mts)
#
# kms = myMap(m_to_km, ms)
# print(kms)

# f = list(map(temp_convert, temp))
# print(f)
#
# mts = list(map(km_to_m, kms))
# print(mts)
#
# kms = list(map(m_to_km, ms))
# print(kms)


f = list(map(lambda c : 9/5 * c + 32, temp))
print(f)

mts = list(map(lambda km : km * 1000, kms))
print(mts)

kms = list(map(lambda m : m / 1000, ms))
print(kms)

# f = []
# for t in temp:
#     f.append(temp_convert(t))
#
# print(f)
#
#
# mts = []
# for k in kms:
#     mts.append(km_to_m(k))
#
# print(mts)