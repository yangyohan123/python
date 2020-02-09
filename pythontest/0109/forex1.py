'''
Created on 2020. 1. 9.

@author: GDJ-19
구구단 출력하기
'''
i, j = 0,0
for i in range(2,10) :
    print(" "*3,i,"단")
    for j in range(2,10) :
        print(i,"X",j,"=",(i*j))
        
