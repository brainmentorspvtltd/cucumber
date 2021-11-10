Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
======= RESTART: C:/Users/ASUS/Desktop/PythonNov/chat_1.py ======
Enter your message : hello
Hello User
>>> 
= RESTART: C:/Users/ASUS/Desktop/PythonNov/chat_1.py
Enter your message : Hello
I don't understand
>>> msg.lower()
'hello'
>>> 
= RESTART: C:/Users/ASUS/Desktop/PythonNov/chat_1.py
Enter your message : HELLO
Hello User
>>> 
= RESTART: C:/Users/ASUS/Desktop/PythonNov/chat_1.py
Enter your message : HELLO
Hello User
>>> 
= RESTART: C:/Users/ASUS/Desktop/PythonNov/chat_1.py
Enter your message : Bye
Bye User
>>> 
= RESTART: C:/Users/ASUS/Desktop/PythonNov/chat_1.py
Enter your message : Bye
Bye User
>>> 
= RESTART: C:/Users/ASUS/Desktop/PythonNov/chat_1.py
Enter your message : Hello
Hello User
Enter your message : hey
I don't understand
Enter your message : bye
Bye User
>>> 
= RESTART: C:/Users/ASUS/Desktop/PythonNov/chat_2.py
Enter your message : hi
I don't understand
Enter your message : hey
I don't understand
Enter your message : bye
Bye User
>>> 
= RESTART: C:/Users/ASUS/Desktop/PythonNov/chat_2.py
Enter your message : hello
Hello User
Enter your message : hi
Hello User
Enter your message : hey
Hello User
Enter your message : bye
Bye User
>>> 
= RESTART: C:/Users/ASUS/Desktop/PythonNov/chat_2.py
Enter your message : hello
Hello User
Enter your message : bye
Bye User
>>> greetingIntent
['hello', 'hi', 'hey', 'hi there', 'hello there']
>>> "hi" in greetingIntent
True
>>> msg = "hello world"
>>> z in msg
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    z in msg
NameError: name 'z' is not defined
>>> 'z' in msg
False
>>> 
= RESTART: C:/Users/ASUS/Desktop/PythonNov/chat_2.py
Enter your message : hello
Hello User
Enter your message : hi
Hello User
Enter your message : bye
Bye User
>>> 
= RESTART: C:/Users/ASUS/Desktop/PythonNov/chat_2.py
Enter your message : hi
hey user
Enter your message : hello
hello there user
Enter your message : hi
hi there user
Enter your message : hey
hi user
Enter your message : bye
Bye User
>>> import time
>>> time.ctime()
'Wed Nov 10 16:25:01 2021'
>>> import datetime
>>> datetime.datetime
<class 'datetime.datetime'>
>>> datetime.datetime.now()
datetime.datetime(2021, 11, 10, 16, 25, 45, 865698)
>>> datetime.datetime.now().date
<built-in method date of datetime.datetime object at 0x0000011A8F42D900>
>>> datetime.datetime.now().date()
datetime.date(2021, 11, 10)
>>> datetime.datetime.now().time()
datetime.time(16, 26, 2, 45668)
>>> from datetime import datetime as dt
>>> dt
<class 'datetime.datetime'>
>>> date = dt.now().date()
>>> time = dt.now().time()
>>> print(date)
2021-11-10
>>> print(time)
16:27:11.865951
>>> date
datetime.date(2021, 11, 10)
>>> date.strftime("%d/%m/%y")
'10/11/21'
>>> date.strftime("%d-%m-%y")
'10-11-21'
>>> date.strftime("%d-%m-%y,%a")
'10-11-21,Wed'
>>> date.strftime("%d-%m-%y,%A")
'10-11-21,Wednesday'
>>> date.strftime("%d %m,%y,%A")
'10 11,21,Wednesday'
>>> date.strftime("%d %b,%y,%A")
'10 Nov,21,Wednesday'
>>> date.strftime("%d %x,%y,%A")
'10 11/10/21,21,Wednesday'
>>> date.strftime("%x")
'11/10/21'
>>> date.strftime("%d %w,%y,%A")
'10 3,21,Wednesday'
>>> date.strftime("%d %b,%y,%A")
'10 Nov,21,Wednesday'
>>> date.strftime("%d %b,%Y,%A")
'10 Nov,2021,Wednesday'
>>> time.strftime("%H:%M:%S")
'16:27:11'
>>> time.strftime("%H:%M:%S,%p")
'16:27:11,PM'
>>> 
======= RESTART: C:/Users/ASUS/Desktop/PythonNov/chat_3.py ======
Enter your message : hi
hi there user
Enter your message : hello
hey user
Enter your message : hey
hi user
Enter your message : date
Date is : 10 Nov,2021,Wednesday
Enter your message : time
Time is : 16:33:47,PM
Enter your message : bye
Bye User
>>> import calendar
>>> print(calendar.calendar(2021))
                                  2021

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3       1  2  3  4  5  6  7       1  2  3  4  5  6  7
 4  5  6  7  8  9 10       8  9 10 11 12 13 14       8  9 10 11 12 13 14
11 12 13 14 15 16 17      15 16 17 18 19 20 21      15 16 17 18 19 20 21
18 19 20 21 22 23 24      22 23 24 25 26 27 28      22 23 24 25 26 27 28
25 26 27 28 29 30 31                                29 30 31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
          1  2  3  4                      1  2          1  2  3  4  5  6
 5  6  7  8  9 10 11       3  4  5  6  7  8  9       7  8  9 10 11 12 13
12 13 14 15 16 17 18      10 11 12 13 14 15 16      14 15 16 17 18 19 20
19 20 21 22 23 24 25      17 18 19 20 21 22 23      21 22 23 24 25 26 27
26 27 28 29 30            24 25 26 27 28 29 30      28 29 30
                          31

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
          1  2  3  4                         1             1  2  3  4  5
 5  6  7  8  9 10 11       2  3  4  5  6  7  8       6  7  8  9 10 11 12
12 13 14 15 16 17 18       9 10 11 12 13 14 15      13 14 15 16 17 18 19
19 20 21 22 23 24 25      16 17 18 19 20 21 22      20 21 22 23 24 25 26
26 27 28 29 30 31         23 24 25 26 27 28 29      27 28 29 30
                          30 31

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3       1  2  3  4  5  6  7             1  2  3  4  5
 4  5  6  7  8  9 10       8  9 10 11 12 13 14       6  7  8  9 10 11 12
11 12 13 14 15 16 17      15 16 17 18 19 20 21      13 14 15 16 17 18 19
18 19 20 21 22 23 24      22 23 24 25 26 27 28      20 21 22 23 24 25 26
25 26 27 28 29 30 31      29 30                     27 28 29 30 31

>>> import os
>>> os.listdir()
['01-basic.py', 'chat_1.py', 'chat_2.py', 'chat_3.py', 'DataTypesMemoryShell.py', 'guess_the_number.py', 'guess_the_number_2.py', 'guess_the_number_3.py', 'if_else_1.py', 'if_else_ladder.py', 'input_function.py', 'loop_1.py', 'nested_loop.py', 'operators.txt', 'prime_number.py', 'prime_number_2.py', 'print_statement.py', 'python_shell_1.py', 'walrus_operator.py', 'while_intro.py']
>>> os.listdir('Songs')
['bang-bang.mp3', 'exception_hierarchy.png', 'Faded.mp3', 'fifa world cup.mp3', 'read_write_1.png', 'song_1.mp3', 'song_2.mp3']
>>> import random
>>> songs = os.listdir('Songs')
>>> random.choice(songs)
'read_write_1.png'
>>> import glob
>>> glob.glob('*.mp3')
[]
>>> os.getcwd()
'C:\\Users\\ASUS\\Desktop\\PythonNov'
>>> os.chdir("Songs")
>>> os.getcwd()
'C:\\Users\\ASUS\\Desktop\\PythonNov\\Songs'
>>> glob.glob('*.mp3')
['bang-bang.mp3', 'Faded.mp3', 'fifa world cup.mp3', 'song_1.mp3', 'song_2.mp3']
>>> songs = glob.glob('*.mp3')
>>> os.startfile(song)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    os.startfile(song)
NameError: name 'song' is not defined
>>> song = random.choice(songs)
>>> os.startfile(song)
>>> song = random.choice(songs)
>>> os.startfile(song)
>>> 
======= RESTART: C:/Users/ASUS/Desktop/PythonNov/chat_3.py ======
Enter your message : hi
hi there user
Enter your message : hey
hello there user
Enter your message : hello
hey user
Enter your message : date
Date is : 10 Nov,2021,Wednesday
Enter your message : play song
Enter your message : bye
Bye User
>>> os.startfile(['song.mp3'])
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    os.startfile(['song.mp3'])
TypeError: startfile: filepath should be string, bytes or os.PathLike, not list
>>> 