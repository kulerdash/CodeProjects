#encoding:utf-8
'''
@File    :   Fibonacci.py
@Time    :   2020/09/10 00:02:16
@Author  :   kulerdash 
@Version :   1.0
@Contact :   thmei0406@icloud.com
@WebSite :   github.com/kulerdash
'''
# Start typing your code from here
x = int(input('How many numbers would you like to see:'))
a = [1, 1, 2]
print(a[0])
if x>1:
    print(a[1])
if x>2:
    print(a[2])
for i in range(3, x):
    a.append(a[i-2]+a[i-1])
    print(a[i])