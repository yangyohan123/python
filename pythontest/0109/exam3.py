'''
Created on 2020. 1. 9.

@author: GDJ-19
숫자를 입력받아 입력수까지 합을 출력하기
'''
num = int(input("숫자:"))
start = 1
result = 0

while start <= num:
    result += start
    start += 1    
print(result)

result = 0
for i in range(1,num+1) :
    result += i
    
print(result)

result = 0
for i in range(0,num+1,2) :
    result += i
print("1부터",num,"까지의 짝수의 합:",result)