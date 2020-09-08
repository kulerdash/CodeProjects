#encoding:utf-8
'''
@File    :   Gcf.py
@Time    :   2020/09/08 15:52:06
@Author  :   kulerdash 
@Version :   1.0
@Contact :   thmei0406@icloud.com
@WebSite :   github.com/kulerdash
'''
# Start typing your code from here
ai, bi = input('Please input two numbers:').split()
a, b = int(ai), int(bi)
mod = a % b
while mod != 0:
    a = b
    b = mod
    mod = a % b
m = b
n = (int(ai) // m) * (int(bi) // m) * m
print('The greatest common divisor is', m)
print('The least common multiple is', n)