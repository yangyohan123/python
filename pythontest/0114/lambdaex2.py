'''
Created on 2020. 1. 14.

@author: GDJ-19
람다식을 이용한 리스트 처리
'''
myList = [1,2,3,4,5]

def add10(num):
    return num + 10

for i in range(len(myList)):
    myList[i] = add10(myList[i])
    
print(myList)

#add10 함수와 같은 기능을 가진 add함수를 람다식으로 구현하기
add = lambda num:num+10
for i in range(len(myList)) :
    myList[i] = (lambda num:num+10)(myList[i])#add(myList[i]) 
    
print(myList)