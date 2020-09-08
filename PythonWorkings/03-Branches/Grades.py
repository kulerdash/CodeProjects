#encoding:utf-8
'''
@File    :   Grades.py
@Time    :   2020/09/08 15:10:46
@Author  :   kulerdash 
@Version :   1.0
@Contact :   thmei0406@icloud.com
@WebSite :   github.com/kulerdash
'''
# Start typing your code from here
g = int(input('Please input your grade:'))
if g >= 90:
    print('A')
elif g >= 80:
    print('B')
elif g >= 70:
    print('C')
elif g >= 60:
    print('D')
else:
    print('E')