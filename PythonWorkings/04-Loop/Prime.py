#encoding:utf-8
'''
@File    :   Prime.py
@Time    :   2020/09/08 15:39:11
@Author  :   kulerdash 
@Version :   1.0
@Contact :   thmei0406@icloud.com
@WebSite :   github.com/kulerdash
'''
# Start typing your code from here
import math as m
x = int(input('Please input a number:'))
t = int(m.sqrt(x))
get = True
if x == 2:
    get = True
elif x % 2 == 0:
    get = False
else:
    for i in range(3, t+1, 2):
        if x % i == 0:
            get = False
            break
if get:
    print(x,'is a prime number.')
else:
    print(x,'is not a prime number.')