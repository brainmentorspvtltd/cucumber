Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text = "hello"
>>> type(test)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    type(test)
NameError: name 'test' is not defined
>>> type(text)
<class 'str'>
>>> text = "hello world"
>>> print(text)
hello world
>>> text
'hello world'
>>> print(text)
hello world
>>> text = 'hello world'
>>> text = '''hello world'''
>>> text = """hello world"""
>>> print(text)
hello world
>>> text = "'hello world'"
>>> print(text)
'hello world'
>>> texpath = "C:\Users\ASUS\Desktop"
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> 
>>> 
>>> text = "Hello \n World"
>>> print(text)
Hello 
 World
>>> path = "C:\new_folder\amit"
>>> print(path)
C:
ew_foldermit
>>> texpath = "C:/Users/ASUS/Desktop"
>>> print(path)
C:
ew_foldermit
>>> print(textpath)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print(textpath)
NameError: name 'textpath' is not defined
>>> path = "C:/Users/ASUS/Desktop"
>>> print(path)
C:/Users/ASUS/Desktop
>>> path = "C:\\Users\\ASUS\\Desktop"
>>> print(path)
C:\Users\ASUS\Desktop
>>> path
'C:\\Users\\ASUS\\Desktop'
>>> path = r"C:\Users\ASUS\Desktop"
>>> path
'C:\\Users\\ASUS\\Desktop'
>>> #raw string
>>> 