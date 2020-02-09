'''
Created on 2020. 1. 9.

@author: GDJ-19
가로 구구단 출력하기
'''
i,j = 0,0
for i in range(2,10):
    print("%5d단%15s"% (i,' '), end="")
print()
for i in range(2,10):
    for j in range(2,10):
        print("%2d X%2d =%3d" % (j,i,(j*i)),end="")
        print("  ",end="")
    print()
