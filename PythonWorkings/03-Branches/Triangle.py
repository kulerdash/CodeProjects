#encoding:utf-8
'''
@File    :   Triangle.py
@Time    :   2020/09/08 15:17:19
@Author  :   kulerdash 
@Version :   1.0
@Contact :   thmei0406@icloud.com
@WebSite :   github.com/kulerdash
'''
# Start typing your code from here
import math as m
ai,bi,ci = input('Please input the three side lengths\
     of the triangle:').split()
a,b,c = int(ai),int(bi),int(ci)
if a+b>c and b+c>a and c+a>b:
    print('The perimeter of this triangle is ',a+b+c)
    p = (a+b+c) / 2
    s = m.sqrt(p*(p-a)*(p-b)*(p-c))
    print('The area of this triangle is %.2f' % (s))
else:
    print('Invalid input')



    
