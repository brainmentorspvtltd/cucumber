Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data = {}
>>> data = dict()
>>> data = {"name" : "Ram", "dept" : "IT"}
>>> data
{'name': 'Ram', 'dept': 'IT'}
>>> data[0]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    data[0]
KeyError: 0
>>> data.keys()
dict_keys(['name', 'dept'])
>>> data["name"]
'Ram'
>>> data["dept"]
'IT'
>>> data["sal"] = 45000
>>> data
{'name': 'Ram', 'dept': 'IT', 'sal': 45000}
>>> data = {"names" : ["Ram", "Shyam"], "sal" : [45000,56000]}
>>> data
{'names': ['Ram', 'Shyam'], 'sal': [45000, 56000]}
>>> data["names"]
['Ram', 'Shyam']
>>> data["sal"]
[45000, 56000]
>>> data["names"][0]
'Ram'
>>> data["sal"][0]
45000
>>> data = [{"name" : "Ram", "dept" : "IT"},{"name" : "Raman", "dept" : "HR"}]
>>> data
[{'name': 'Ram', 'dept': 'IT'}, {'name': 'Raman', 'dept': 'HR'}]
>>> data[0]
{'name': 'Ram', 'dept': 'IT'}
>>> data[0]["name"]
'Ram'
>>> data[1]
{'name': 'Raman', 'dept': 'HR'}
>>> dir(data)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> data = {"name" : "Ram", "dept" : "IT"}
>>> dir(data)
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> data.keys()
dict_keys(['name', 'dept'])
>>> data.values()
dict_values(['Ram', 'IT'])
>>> data.items()
dict_items([('name', 'Ram'), ('dept', 'IT')])
>>> data["name"]
'Ram'
>>> data["age"]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    data["age"]
KeyError: 'age'
>>> data.get("name")
'Ram'
>>> data.get("age")
>>> data.get("age","Not available")
'Not available'
>>> data.get("name")
'Ram'
>>> data.get("age","Not available")
'Not available'
>>> details = {"address":"Delhi","ph":898989999}
>>> data.update(details)
>>> data
{'name': 'Ram', 'dept': 'IT', 'address': 'Delhi', 'ph': 898989999}
>>> data.pop()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    data.pop()
TypeError: pop expected at least 1 argument, got 0
>>> data.pop("address")
'Delhi'
>>> data
{'name': 'Ram', 'dept': 'IT', 'ph': 898989999}
>>> data.popitem()
('ph', 898989999)
>>> data
{'name': 'Ram', 'dept': 'IT'}
>>> data.setdefault("address")
>>> data
{'name': 'Ram', 'dept': 'IT', 'address': None}
>>> data["address"] = "Delhi"
>>> data
{'name': 'Ram', 'dept': 'IT', 'address': 'Delhi'}
>>> data.setdefault("ph",998988899)
998988899
>>> data
{'name': 'Ram', 'dept': 'IT', 'address': 'Delhi', 'ph': 998988899}
>>> data.fromkeys(["name","dept","ph"])
{'name': None, 'dept': None, 'ph': None}
>>> for i in range(len(data)):
	print(data[i])

	
Traceback (most recent call last):
  File "<pyshell#51>", line 2, in <module>
    print(data[i])
KeyError: 0
>>> for key in data:
	print(key)

	
name
dept
address
ph
>>> for key in data:
	print(key, data[key])

	
name Ram
dept IT
address Delhi
ph 998988899
>>> for val in data.values():
	print(val)

	
Ram
IT
Delhi
998988899
>>> data = {i : i**2 for i in range(1,10)}
>>> data
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
>>> 