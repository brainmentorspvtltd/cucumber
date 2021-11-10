Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text = "hello world this is Python Programming"
>>> len(text)
38
>>> text[0]
'h'
>>> text[1]
'e'
>>> text[10]
'd'
>>> text[-1]
'g'
>>> text[-2]
'n'
>>> text[-20]
's'
>>> text[0:4]
'hell'
>>> text[10:20]
'd this is '
>>> text[10:30]
'd this is Python Pro'
>>> text
'hello world this is Python Programming'
>>> text[10:0]
''
>>> text[10:0:1]
''
>>> text[10:0:-1]
'dlrow olle'
>>> text[10::-1]
'dlrow olleh'
>>> text[0:]
'hello world this is Python Programming'
>>> text[:10]
'hello worl'
>>> text[:]
'hello world this is Python Programming'
>>> text[0:20:2]
'hlowrdti s'
>>> text[::-1]
'gnimmargorP nohtyP si siht dlrow olleh'
>>> text.lower()
'hello world this is python programming'
>>> text.upper()
'HELLO WORLD THIS IS PYTHON PROGRAMMING'
>>> text.capitalize()
'Hello world this is python programming'
>>> text.title()
'Hello World This Is Python Programming'
>>> text.swapcase()
'HELLO WORLD THIS IS pYTHON pROGRAMMING'
>>> text.count('o')
4
>>> text.index('o')
4
>>> text.index('o',0)
4
>>> text.index('o',5)
7
>>> text.index('o',8)
24
>>> text.index('o',25)
29
>>> text.rindex('o')
29
>>> text.find('o')
4
>>> text.find('o',5)
7
>>> text.index('z')
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    text.index('z')
ValueError: substring not found
>>> text.find('z')
-1
>>> text.rfind('z')
-1
>>> text.rfind('e')
1
>>> text.replace('h','i')
'iello world tiis is Pytion Programming'
>>> text
'hello world this is Python Programming'
>>> text.find('is')
14
>>> text.count('is')
2
>>> text.startswith('h')
True
>>> text.endswith('h')
False
>>> text.endswith('s')
False
>>> text.encode()
b'hello world this is Python Programming'
>>> text.islower()
False
>>> text.isalpha()
False
>>> text.isalnum()
False
>>> text.isprintable()
True
>>> text.isspace()
False
>>> text.split()
['hello', 'world', 'this', 'is', 'Python', 'Programming']
>>> text.split(',')
['hello world this is Python Programming']
>>> text.split()
['hello', 'world', 'this', 'is', 'Python', 'Programming']
>>> text.partition(' ')
('hello', ' ', 'world this is Python Programming')
>>> text = 'hello world, this is Python Programming'
>>> text.partition(',')
('hello world', ',', ' this is Python Programming')
>>> text.strip()
'hello world, this is Python Programming'
>>> text = "  hello   "
>>> text.strip()
'hello'
>>> 