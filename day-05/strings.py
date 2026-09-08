Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#int float str list tuple set dist
x = input ()
gfcsdgtyrgfue
x
'gfcsdgtyrgfue'
name = input()
dhana
name
'dhana'
name = input ("Enter your name: ")
Enter your name: subbu
name
'subbu'
age = input("Enter the age:")
Enter the age:20
age
'20'
type(age)
<class 'str'>
<class 'str'>
SyntaxError: invalid syntax
name = input("Enetr the names: ")
Enetr the names: dimple subbu charan
names
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    names
NameError: name 'names' is not defined. Did you mean: 'name'?
name = input ("Enter the names: ")
Enter the names: dhana subbu
names
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    names
NameError: name 'names' is not defined. Did you mean: 'name'?
names = input("Enter the name: ").split
Enter the name: 1 2 3 4 5 6
names
<built-in method split of str object at 0x0000025248D5BEF0>
names = input ("Enter the name: ").split()
Enter the name: 1 2 3 4 54 5
names
['1', '2', '3', '4', '54', '5']
map(int,names)
<map object at 0x000002524651DE00>
list (map(int,names))
[1, 2, 3, 4, 54, 5]
vales = list(map(input().split()))
1 2 34 5 5 6556754
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    vales = list(map(input().split()))
TypeError: map() must have at least two arguments.
values = list(map (input().split()))
1 2 34 5 5 6556754
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    values = list(map (input().split()))
TypeError: map() must have at least two arguments.
values = list(map(int,input().split()))
1 2 34 5 5 6556754
values
[1, 2, 34, 5, 5, 6556754]

values = list (map(float,input().split()))
1 2 3454 5463.23
values
[1.0, 2.0, 3454.0, 5463.23]
names = tuple(input("Enter the namrs:").split()))
SyntaxError: unmatched ')'
names = tuple(inputI("Enter the names:").split()))
SyntaxError: unmatched ')'
values = tuple(map(float,input().split()))
567 5678 567
values
(567.0, 5678.0, 567.0)
names = set(map(int,input().split()))
1 2 4 4
values
(567.0, 5678.0, 567.0)
a,b = [1,2]
a
1
b
2
a,b = (1,2)
a
1
b
2
email,password = input("Enter the email and password:").split()
Enter the email and password: dhanalakshmigorrela798@gmail.com
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    email,password = input("Enter the email and password:").split()
ValueError: not enough values to unpack (expected 2, got 1)
email, password = input("Enter the email and password:").split()
Enter the email and password:dhanalakshmi@gmail.com
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    email, password = input("Enter the email and password:").split()
ValueError: not enough values to unpack (expected 2, got 1)
email,password = input("Enter the email and password:").split()
Enter the email and password:dhana@codegnan.com 123456
email
'dhana@codegnan.com'
password
'123456'
a,b,c = list(map(input().split()))
1 2 3
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    a,b,c = list(map(input().split()))
TypeError: map() must have at least two arguments.
a,b,c = list(map(int,input().split()))
1 2 3
a
1
b
2
c
3
name,marks = input().split()
dhana 75
name
'dhana'
>>> marks
'75'
>>> int(marks)
75
>>> e = eval(input())
12.34
>>> e
12.34
>>> e = eval(input())
"dhana"
>>> e
'dhana'
>>> e = eval(input())
[1,2,3,4,5,6]
>>> e
[1, 2, 3, 4, 5, 6]
>>> e = eval(input())
true
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    e = eval(input())
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> e = eval (input())
{1,2,3,4,5}
>>> e
{1, 2, 3, 4, 5}
>>> e = eval (input())
{1:1,2:2,3:3}
>>> e = evl (input())
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    e = evl (input())
NameError: name 'evl' is not defined. Did you mean: 'eval'?
>>> e = eval (input())
2+3*4+5*8
>>> e
54
