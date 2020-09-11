#encoding:utf-8
'''
@File    :   Prime3.py
@Time    :   2020/09/11 22:50:56
@Author  :   kulerdash 
@Version :   1.0
@Contact :   thmei0406@icloud.com
@WebSite :   github.com/kulerdash
'''
# Start typing your code from here
import math as m
def is_prime(x):
    t = int(m.sqrt(x))
    get = True
    if x == 2:
        get = True
    elif x <= 1:
        get = False
    elif x % 2 == 0:
        get = False
    else:
        for i in range(3, t+1, 2):
            if x % i == 0:
                get = False
                break
    return get

u = int(input('Please input your number:'))
if is_prime(u):
    print(u,'is a prime number.')
else:
    print(u,'is not a prime number.')