Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 10
>>> type(x)
<class 'int'>
>>> x = 10,
>>> type(x)
<class 'tuple'>
>>> x
(10,)
>>> x = 10,20,30,40
>>> x
(10, 20, 30, 40)
>>> x = (10,20,30,40)
>>> x
(10, 20, 30, 40)
>>> x[0] = 100
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    x[0] = 100
TypeError: 'tuple' object does not support item assignment
>>> del x[0]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    del x[0]
TypeError: 'tuple' object doesn't support item deletion
>>> data = name, sal, dept = "Ram", 45000, "IT"
>>> data
('Ram', 45000, 'IT')
>>> name
'Ram'
>>> sal
45000
>>> dept
'IT'
>>> data
('Ram', 45000, 'IT')
>>> name, sal, dept = data
>>> name
'Ram'
>>> sal
45000
>>> dept
'IT'
>>> name, sal = data
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    name, sal = data
ValueError: too many values to unpack (expected 2)
>>> name, sal, age, dept = data
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    name, sal, age, dept = data
ValueError: not enough values to unpack (expected 4, got 3)
>>> name, *details = data
>>> name
'Ram'
>>> details
[45000, 'IT']
>>> 