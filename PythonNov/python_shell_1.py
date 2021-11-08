Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 10
>>> x = x + 1
>>> x
11
>>> x += 1
>>> x
12
>>> x -= 1
>>> x *= 2
>>> x
22
>>> x //= 2
>>> x
11
>>> x
11
>>> y = 12
>>> x > y
False
>>> x < y
True
>>> x == y
False
>>> x != y
True
>>> x >= y
False
>>> x <= y
True
>>> in
SyntaxError: invalid syntax
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> 
>>> 
>>> 
>>> 
>>> for = "hello"
SyntaxError: invalid syntax
>>> len(keyword.kwlist)
36
>>> .x = 10
SyntaxError: invalid syntax
>>> _x = 10
>>> x.name = 10
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    x.name = 10
AttributeError: 'int' object has no attribute 'name'
>>> x_name = "ravi"
>>> x_name
'ravi'
>>> x1 = 12
>>> 