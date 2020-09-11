#encoding:utf-8
'''
@File    :   Palindrome.py
@Time    :   2020/09/11 21:53:24
@Author  :   kulerdash 
@Version :   1.0
@Contact :   thmei0406@icloud.com
@WebSite :   github.com/kulerdash
'''
# Start typing your code from here
def length(x):
    get = True
    i = 0
    while get:
        i = i+1
        t = x//(10**i)
        if t == 0:
            get = False
    return i

def palin(x):
    l = length(x)
    fa = True
    for i in range(1,l+1):
        if (x%(10**i))//(10**(i-1)) != (x%(10**(l-i+1)))//(10**(l-i)):
            fa = False
            break
    return fa

a = int(input("Please input your number:"))
if palin(a):
    print(a,"is a Palindrome number.")
else:
    print(a,"is not a Palindrome number.")