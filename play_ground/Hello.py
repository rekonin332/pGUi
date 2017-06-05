# -*- coding:utf8 -*-
'''
Created on 2017年5月18日

@author: Todd
'''

from copy import deepcopy
from collections import OrderedDict

class PythonProjects():
    def __init__(self, msg):
        self.msg = msg
        self.print_message()
    
    def print_message(self):
        print(self.msg)
        
    
class ChildPythonProjects(PythonProjects):
    def print_message(self):
        print("hi", self.msg);
        
        
# from urllib import request
# 
# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', data.decode('utf-8'))        
# 
# def tranform():
#     for i in range(10):
#         print(i)
        
# tranform()

if __name__ == '__main__':
#     p = PythonProjects('sdfsdf')
#     ChildPythonProjects('eee')
    
    d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
    
    
    od1 = OrderedDict(d)
    print(od1)
    print()
    for k, v in od1.items():
        print(k, v)    
    
    od = OrderedDict(sorted(d.items(), key=lambda t: t[0]))

    for k, v in od.items():
        print(k, v)
