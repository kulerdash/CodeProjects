#encoding:utf-8
'''
@File    :   PerfectNumber.py
@Time    :   2020/09/11 15:54:28
@Author  :   kulerdash 
@Version :   1.0
@Contact :   thmei0406@icloud.com
@WebSite :   github.com/kulerdash
'''
# Start typing your code from here
x = int(input("Please input a number:"))
for i in range(3, x+1):
    y = 0
    for j in range(1, i // 2+1):
        if i % j == 0:
            y = y + j
    if i == y:
        print(i)