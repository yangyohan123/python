'''
Created on 2020. 1. 15.

@author: GDJ-19
컴프리핸션 예제
'''
numbers =[]
for n in range(1, 11) :
    numbers.append(n)
print(numbers)

# comprehenstion 방식
print([x for x in range(1,11)])

numlist = [x for x in range(1, 11)]
print(numlist)

# 1~10 까지 짝수 리스트 생성
evenlist = []
for n in range(1, 11) :
    if n % 2 == 0 :
        evenlist.append(n)
print(evenlist)
evenlist = [x for x in range(1,11) if x % 2 == 0]
print(evenlist)

#2의 배수 이면서 3의 백수인 리스트 생성
evenlist = [x for x in range(1,11) if x % 2 == 0 if x % 3 == 0]
print(evenlist)

#중첩사용 컴프리핸션
matrix = [[1,2,3],[4,5,6],[7,8,9]]
list1 = [x for row in matrix for x in row]
print(list1)

# set 컴프리핸션
set1 = {x**2 for x in [1,2,3]}
print(set1)

#1부터 10까지의 수 중 짝수의 제곱을 출력하기 : 컴프리핸션 문법 이용하기
set2 = {x**2 for x in range(1,11) if x % 2 == 0}
print(sorted(set2))

