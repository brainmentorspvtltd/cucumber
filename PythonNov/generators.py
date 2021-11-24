Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def add():
	return "Hello"

>>> for msg in add():
	print(msg)

	
H
e
l
l
o
>>> for msg in add:
	print(msg)

	
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    for msg in add:
TypeError: 'function' object is not iterable
>>> iter(add)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    iter(add)
TypeError: 'function' object is not iterable
>>> def counter():
	x = 0
	while True:
		x += 1
		return x

	
>>> counter()
1
>>> counter()
1
>>> x = 0
>>> def counter(y):
	while True:
		y += 1
		return y

	
>>> counter(x)
1
>>> counter(x)
1
>>> x = counter(x)
>>> x
1
>>> x = counter(x)
>>> x
2
>>> x = counter(x)
>>> x
3
>>> def counter(y):
	x = 0
	while True:
		x += 1
		return x

	
>>> def counter():
	x = 0
	while True:
		x += 1
		return x

	
>>> counter()
1
>>> counter()
1
>>> def counter():
	x = 0
	while True:
		x += 1
		yield x

		
>>> counter
<function counter at 0x0000017A0A437E50>
>>> counter()
<generator object counter at 0x0000017A0A3B3EB0>
>>> next(counter())
1
>>> next(counter())
1
\
>>> next(counter())
1
>>> views = counter()
>>> next(views)
1
>>> next(views)
2
>>> next(views)
3
>>> def counter():
	x = 0
	while True:
		x += 1
		return x

	
>>> counter()
1
>>> counter()
1
>>> def counter():
	x = 0
	while True:
		x += 1
		yield x

		
>>> counter()
<generator object counter at 0x0000017A0A44DAC0>
>>> count = counter()
>>> count
<generator object counter at 0x0000017A0A44DBA0>
>>> next(count)
1
>>> next(count)
2
>>> next(count)
3
>>> def counter():
	x = 0
	while True:
		x += 1
		print("Before")
		yield x
		print("After")

		
>>> count = counter()
>>> next(count)
Before
1
>>> next(count)
After
Before
2
>>> 
>>> next(count)
After
Before
3
>>> next(count)
After
Before
4
>>> def counter():
	x,y = 0,0 
	while True:
		x += 1
		y += 1
		yield x,y

		
>>> counter()
<generator object counter at 0x0000017A0A44DBA0>
>>> c = counter()
>>> next(c)
(1, 1)
>>> next(c)
(2, 2)
>>> def counter():
	x,y = 0,0
	while True:
		x += 1
		y = x ** 2
		yield x,y

		
>>> c = counter()
>>> next(c)
(1, 1)
>>> next(c)
(2, 4)
>>> next(c)
(3, 9)
>>> next(c)
(4, 16)
>>> (3, 9)
(3, 9)
>>> import iterators
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    import iterators
ModuleNotFoundError: No module named 'iterators'
>>> import iterators
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    import iterators
ModuleNotFoundError: No module named 'iterators'
>>> import iterator
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    import iterator
ModuleNotFoundError: No module named 'iterator'
>>> import collections
>>> iter_val = "Hello World"
>>> iter(iter_val)
<str_iterator object at 0x0000017A0A42FAF0>
>>> iter(counter)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    iter(counter)
TypeError: 'function' object is not iterable
>>> iter(counter())
<generator object counter at 0x0000017A0A44DC80>
>>> lambda x,y : x + y
<function <lambda> at 0x0000017A0A4591F0>
>>> def add(x,y):
	return x + y

>>> calc(6,6)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    calc(6,6)
NameError: name 'calc' is not defined
>>> add(6,6)
12
>>> (lambda x,y : x + y)(54,6)
60
>>> add = lambda x,y : x + y
>>> add(4,6)
10
>>> 