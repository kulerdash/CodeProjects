#encoding:utf-8
'''
@File    :   Trilogo.py
@Time    :   2020/09/08 16:15:30
@Author  :   kulerdash 
@Version :   1.0
@Contact :   thmei0406@icloud.com
@WebSite :   github.com/kulerdash
'''
# Start typing your code from here
x = int(input('Please input your number:'))
for i in range(1, x+1):
    for j in range (1, i+1):
        print("*", end="")
    print()
for i in range(1, x+1):
    for j in range(1, x-i+1):
        print(" ", end="")
    for j in range(1, i+1):
        print("*", end="")
    print()
for i in range(1, x+1):
    for j in range(1, x-i+1):
        print(" ", end="")
    for j in range(1, i*2):
        print("*", end="")
    for j in range(1, x-i+1):
        print(" ", end="")
    print()