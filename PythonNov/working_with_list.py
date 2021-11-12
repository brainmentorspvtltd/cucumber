Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = list()
>>> x = []
>>> type(x)
<class 'list'>
>>> x = [2,4,5,"python",56.55]
>>> len(x)
5
>>> x[0]
2
>>> x[0:4]
[2, 4, 5, 'python']
>>> x[-1]
56.55
>>> dir(x)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> x = []
>>> x.append(45)
>>> x
[45]
>>> x.append(34)
>>> x.append(10)
>>> x.append(20)
>>> x
[45, 34, 10, 20]
>>> x.pop()
20
>>> x
[45, 34, 10]
>>> x.append(6,4,6,8,3,7,8)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    x.append(6,4,6,8,3,7,8)
TypeError: list.append() takes exactly one argument (7 given)
>>> x.append([6,4,6,8,3,7,8])
>>> x
[45, 34, 10, [6, 4, 6, 8, 3, 7, 8]]
>>> x.pop()
[6, 4, 6, 8, 3, 7, 8]
>>> x
[45, 34, 10]
>>> x.extend([6,4,6,8,3,7,8])
>>> x
[45, 34, 10, 6, 4, 6, 8, 3, 7, 8]
>>> x.pop()
8
>>> x
[45, 34, 10, 6, 4, 6, 8, 3, 7]
>>> x.pop(5)
6
>>> x
[45, 34, 10, 6, 4, 8, 3, 7]
>>> x.insert(3,100)
>>> x
[45, 34, 10, 100, 6, 4, 8, 3, 7]
>>> x.remove(5)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    x.remove(5)
ValueError: list.remove(x): x not in list
>>> x.remove(4)
>>> x
[45, 34, 10, 100, 6, 8, 3, 7]
>>> x.index(5)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    x.index(5)
ValueError: 5 is not in list
>>> x.count(5)
0
>>> x.count(10)
1
>>> x
[45, 34, 10, 100, 6, 8, 3, 7]
>>> x.index(10)
2
>>> x.sort()
>>> x
[3, 6, 7, 8, 10, 34, 45, 100]
>>> x.sort(reverse=True)
>>> x
[100, 45, 34, 10, 8, 7, 6, 3]
>>> sorted
<built-in function sorted>
>>> x
[100, 45, 34, 10, 8, 7, 6, 3]
>>> sorted(x)
[3, 6, 7, 8, 10, 34, 45, 100]
>>> x
[100, 45, 34, 10, 8, 7, 6, 3]
>>> x.sort()
>>> x
[3, 6, 7, 8, 10, 34, 45, 100]
>>> x = []
>>> for i in range(1,51):
	if i % 2 != 0:
		x.append(i)

		
>>> x
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
>>> x = [i for i in range(1,11)]
>>> x
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> x = [i for i in range(1,11) if i % 2 != 0]
>>> x
[1, 3, 5, 7, 9]
>>> x = [[i,j] for i in range(5) for j in range(5)]
>>> x
[[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
>>> x = [i ** 2 for i in range(5)]
>>> x
[0, 1, 4, 9, 16]
>>> noprime = set(j for i in range(2,10) for j in range(i*2, 50,i))
>>> noprime
{4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49}
>>> primeNumbers = [x for x in range(2,50) if x not in noprime]
>>> primeNumbers
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
>>> noprime = []
>>> for i in range(2,10):
	for j in range(i*2, 50, i):
		noprime.append(j)

		
>>> noprime
[4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 10, 15, 20, 25, 30, 35, 40, 45, 12, 18, 24, 30, 36, 42, 48, 14, 21, 28, 35, 42, 49, 16, 24, 32, 40, 48, 18, 27, 36, 45]
>>> set(noprime)
{4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49}
>>> 