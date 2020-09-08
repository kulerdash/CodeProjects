#encoding:utf-8
'''
@File    :   Imperial.py
@Time    :   2020/09/08 15:00:27
@Author  :   kulerdash 
@Version :   1.0
@Contact :   thmei0406@icloud.com
@WebSite :   github.com/kulerdash
'''
# Start typing your code from here
l = float(input('Please input the length:'))
unit = str(input('Please input the unit:'))
if unit == 'cm':
    conv = l / 2.54
    print('%.2fin' % (conv))
elif unit == 'in':
    conv = l * 2.54
    print('%.2fcm' % (conv))
else:
    print('ERROR!')