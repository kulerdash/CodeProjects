#encoding:utf-8
'''
@File    :   Radius.py
@Time    :   2020/09/08 14:39:53
@Author  :   kulerdash 
@Version :   1.0
@Contact :   thmei0406@icloud.com
@WebSite :   github.com/kulerdash
'''
# Start typing your code from here
import math
r = float(input('Please input the radius:'))
c = math.pi * 2 * r
s = math.pi * (r ** 2)
print('C=%.2f, S=%.2f' % (c,s))