Python 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sys
>>> x = 10
>>> sys.getsizeof(x)
28
>>> x = 0
>>> sys.getsizeof(x)
24
>>> sys.getsizeof(0)
24
>>> sys.getsizeof(1)
28
>>> sys.getsizeof(2)
28
>>> sys.getsizeof(100)
28
>>> sys.getsizeof(10000)
28
>>> sys.getsizeof(100000)
28
>>> sys.getsizeof(1000000)
28
>>> sys.getsizeof(10000000)
28
>>> sys.getsizeof(100000000)
28
>>> sys.getsizeof(1000000000)
28
>>> sys.getsizeof(10000000000)
32
>>> id(x)
140730366498544
>>> x
0
>>> x = 1
>>> id(x)
140730366498576
>>> dir(x)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> x = ""
>>> sys.getsizeof(x)
49
>>> sys.getsizeof("")
49
>>> sys.getsizeof("h")
50
>>> sys.getsizeof("he")
51
>>> sys.getsizeof("hel")
52
>>> sys.getsizeof("hell")
53
>>> sys.getsizeof("hello")
54
>>> type(x)
<class 'str'>
>>> type(23)
<class 'int'>
>>> type(23.44)
<class 'float'>
>>> isinstance(12,int)
True
>>> 