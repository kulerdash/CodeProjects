#encoding:utf-8
'''
@File    :   Year.py
@Time    :   2020/09/08 14:51:23
@Author  :   kulerdash 
@Version :   1.0
@Contact :   thmei0406@icloud.com
@WebSite :   github.com/kulerdash
'''
# Start typing your code from here
y = int(input('Which year would you like to check? Input:'))
if y % 400 == 0:
    ans = True
elif y % 100 == 0:
    ans = False
elif y % 4 == 0:
    ans = True
else:
    ans = False
if ans:
    print(y,' is a leap year.')
else:
    print(y,' is an average year.')