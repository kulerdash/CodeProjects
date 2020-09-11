#encoding:utf-8
'''
@File    :   Palinprime.py
@Time    :   2020/09/11 22:57:20
@Author  :   kulerdash 
@Version :   1.0
@Contact :   thmei0406@icloud.com
@WebSite :   github.com/kulerdash
'''
# Start typing your code from here
from Palindrome import palin, length
from Prime3 import is_prime

z = int(input('Please input your number:'))
if palin(z) and is_prime(z):
    print('Yes.')
else:
    print('No.')
