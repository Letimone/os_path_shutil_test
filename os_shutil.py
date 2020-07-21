# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 19:39:14 2020

@author: tagia
"""


import os
import shutil

os.chdir('d:\\testprogrammation')
#os.rename('test8.csv', 'test.csv')

result = []

for root, dir, files in os.walk('d:'):
    if os.path.isfile('test.csv'):
        result.append('test.csv')
        break
       

print(result) 

with os.scandir('d:\\testprogrammation') as dir_content:
    recent = 0
    recent_file = ['un']
    for entry in dir_content:
        info = entry.stat()
        if info.st_mtime > recent:
            recent_file[0] = entry.name
            recent = info.st_mtime
    result.append(recent_file[0])
print(result)

#shutil.copy('d:\\testprogrammation\monfichiertextdevalidation.txt', 'd:\\testprogrammation\Class_prat')
shutil.copytree('d:\\testprogrammation\repsource', 'repdest')