Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data = [4,3,5,7,23,45,7,8,5,7]
>>> sorted(data)
[3, 4, 5, 5, 7, 7, 7, 8, 23, 45]
>>> data = [["John",45000],["Mac",54000],["Brad",25000]]
>>> sorted(data)
[['Brad', 25000], ['John', 45000], ['Mac', 54000]]
>>> sorted(data, key=1)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    sorted(data, key=1)
TypeError: 'int' object is not callable
>>> x = 1
>>> x()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    x()
TypeError: 'int' object is not callable
>>> def func(x):
	return x[1]

>>> sorted(data, key=func)
[['Brad', 25000], ['John', 45000], ['Mac', 54000]]
>>> data = [["John",45000],["Mac",54000],["Brad",25000],["Tom",20000]]
>>> sorted(data, key=func)
[['Tom', 20000], ['Brad', 25000], ['John', 45000], ['Mac', 54000]]
>>> sorted(data, key=func, reverse=True)
[['Mac', 54000], ['John', 45000], ['Brad', 25000], ['Tom', 20000]]
>>> 
>>> 
>>> for x in data:
	print(x)

	
['John', 45000]
['Mac', 54000]
['Brad', 25000]
['Tom', 20000]
>>> data = [{"name":"Ram","sal":45000},{"name":"Shyam","sal":90000},{"name":"Mohan","sal":25000}]
>>> sorted(data)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    sorted(data)
TypeError: '<' not supported between instances of 'dict' and 'dict'
>>> def func(x):
	return x["sal"]

>>> sorted(data, key=func)
[{'name': 'Mohan', 'sal': 25000}, {'name': 'Ram', 'sal': 45000}, {'name': 'Shyam', 'sal': 90000}]
>>> sorted(data, key=func, reverse=True)
[{'name': 'Shyam', 'sal': 90000}, {'name': 'Ram', 'sal': 45000}, {'name': 'Mohan', 'sal': 25000}]
>>> 