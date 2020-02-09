'''
Created on 2020. 1. 21.

@author: GDJ-19
'''

import os.path
file= "C:\\Data\\Python\\nofile.txt"
file="csvex1.py"
file="../0115"
file = "../1015"
if os.path.isfile(file):
    print("Yes. it is a file") # 파일
elif os.path.isdir(file) :
    print("Yes. it is a directory") # 디렉터리(폴더)
elif os.path.exists(file):
    print("Something exist") # 파일, 디렉터리도 아닌 것 
else :
    print("Nothing") # 존재하지않는 