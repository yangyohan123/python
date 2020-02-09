'''
Created on 2020. 1. 15.

@author: GDJ-19
로또번호 생성기
'''
import random
def getNumber():
    return random.randrange(1,46)

#딕셔너리이기때문에 set으로 변환 : 중복제거하기위해
lotto= set({getNumber() for x in range(1, 7)})

lotto1 = set([])
while len(lotto1) < 6 :
    #lotto1.add(random.randrange(1,46))
    lotto1.add(getNumber())
print("추첨된 로또 번호=>", sorted(lotto))
print("추첨된 로또 번호=>", sorted(lotto1))