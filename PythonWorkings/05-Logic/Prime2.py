#encoding:utf-8
'''
@File    :   Prime2.py
@Time    :   2020/09/11 16:13:00
@Author  :   kulerdash 
@Version :   1.0
@Contact :   thmei0406@icloud.com
@WebSite :   github.com/kulerdash
'''
# Start typing your code from here
import math as m
x = int(input("Please input a number:"))
if x >= 2:
    print(2)
for i in range (3, x+1, 2):
    t = int(m.sqrt(i))
    get = True
    for j in range(3, t+1, 2):
        if i % j == 0:
            get = False
            break
    if get:
        print(i)