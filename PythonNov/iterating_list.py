Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> names = ["John","Mac","Sam","Tom"]
>>> for i in range(len(names)):
	print(names[i])

	
John
Mac
Sam
Tom
>>> for name in names:
	print(name)

	
John
Mac
Sam
Tom
>>> enumerate(names)
<enumerate object at 0x0000015BC0D4B100>
>>> for i, name in enumerate(names):
	print(i, name)

	
0 John
1 Mac
2 Sam
3 Tom
>>> for name in enumerate(names):
	print(name)

	
(0, 'John')
(1, 'Mac')
(2, 'Sam')
(3, 'Tom')
>>> 