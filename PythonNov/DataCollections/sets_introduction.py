Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = {}
>>> type(x)
<class 'dict'>
>>> x = {3,2,5,6,7,7,23,4,4,5,8,12,2,3,54,67,9}
>>> x
{2, 3, 4, 5, 6, 7, 8, 67, 9, 12, 54, 23}
>>> y = {34,3,4,67,8,9,5,3,2,5,78,3}
>>> y
{34, 67, 3, 4, 5, 2, 8, 9, 78}
>>> x & y
{2, 3, 67, 4, 5, 8, 9}
>>> x | y
{2, 3, 4, 5, 6, 7, 8, 67, 9, 12, 78, 23, 34, 54}
>>> x - y
{6, 7, 12, 54, 23}
>>> x.intersection(y)
{2, 3, 67, 4, 5, 8, 9}
>>> x.union(y)
{2, 3, 4, 5, 6, 7, 8, 67, 9, 12, 78, 23, 34, 54}
>>> x.difference(y)
{6, 7, 12, 54, 23}
>>> z = {3,45,6,7,'hello'}
>>> z
{3, 6, 7, 'hello', 45}
>>> z = {3,45,6,7,'hello',[3,4],[23,23],(3,5)}
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    z = {3,45,6,7,'hello',[3,4],[23,23],(3,5)}
TypeError: unhashable type: 'list'
>>> z = {3,45,6,7,'hello',(3,4),(23,23),(3,5)}
>>> z = {3,5,6,{4,6,8},23}
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    z = {3,5,6,{4,6,8},23}
TypeError: unhashable type: 'set'
>>> z = {2,3,5,{"name":"Ram"},45}
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    z = {2,3,5,{"name":"Ram"},45}
TypeError: unhashable type: 'dict'
>>> z[1]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    z[1]
TypeError: 'set' object is not subscriptable
>>> z.pop()
(23, 23)
>>> z
{3, (3, 4), 6, 7, 45, 'hello', (3, 5)}
>>> z = {3,5,6,{4,6,8},23}
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    z = {3,5,6,{4,6,8},23}
TypeError: unhashable type: 'set'
>>> z = {3,5,6,4,6,8,23}
>>> z.pop()
3
>>> z = {3,5,6,4,6,8,23}
>>> z
{3, 4, 5, 6, 23, 8}
>>> z.pop()
3
>>> z
{4, 5, 6, 23, 8}
>>> z.add(10)
>>> z
{4, 5, 6, 23, 8, 10}
>>> z.add(20)
>>> z
{4, 5, 6, 23, 8, 20, 10}
>>> z.add(30)
>>> z
{4, 5, 6, 8, 10, 20, 23, 30}
>>> z.update([2,3,4])
>>> z
{2, 3, 4, 5, 6, 8, 10, 20, 23, 30}
>>> z.discard()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    z.discard()
TypeError: set.discard() takes exactly one argument (0 given)
>>> z.discard(10)
>>> z
{2, 3, 4, 5, 6, 8, 20, 23, 30}
>>> z.discard([4,5,6])
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    z.discard([4,5,6])
TypeError: unhashable type: 'list'
>>> z.discard({4,5,6})
>>> z
{2, 3, 4, 5, 6, 8, 20, 23, 30}
>>> 