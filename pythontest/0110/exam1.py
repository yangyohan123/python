'''
Created on 2020. 1. 10.

@author: GDJ-19
리스트문제:
aa,bb 매열을 생성하고,
aa 배열은 0부터 짝수 100개를 저장하고
bb 배열은 aa 배열의 역순으로 값을 저장하기.
aa[0] ~ aa[9], bb[99] ~ bb[90] 값을 출력하기
'''
#0,0 1,2 2,4 3,6
aa = []
bb = []
value = 0
for i in range(0,100) :
    aa.append(value)
    aa[i] = i*2
    bb.append(aa[i])
    
bb.reverse()


for i in range(0,10) :
    print("aa[%2d]=%3d"% (i,aa[i]),end=",")
print()

for i in range(99,89,-1) :
    print("bb[%2d]=%3d"% (i,bb[i]),end=",")

