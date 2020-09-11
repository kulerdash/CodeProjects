#encoding:utf-8
'''
@File    :   gcf2.py
@Time    :   2020/09/11 21:39:23
@Author  :   kulerdash 
@Version :   1.0
@Contact :   thmei0406@icloud.com
@WebSite :   github.com/kulerdash
'''
# Start typing your code from here
def swap(x,y):
    mid = x
    x = y
    y = mid

def gcd(x,y):
    if x < y:
        swap(x,y)
    mod = x % y
    while mod != 0:
        x = y
        y = mod
        mod = x % y
    return y


def lcm(x,y):
    med = gcd(x,y)
    mad = (x // med) * (y // med) * med
    return mad

ai, bi = input('Please input two numbers:').split()
a, b = int(ai), int(bi)
m = gcd(a,b)
n = lcm(a,b)
print('The greatest common divisor is', m)
print('The least common multiple is', n)