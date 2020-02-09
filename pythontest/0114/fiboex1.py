'''
Created on 2020. 1. 14.

@author: GDJ-19
피보너치 수열 구하기

'''

def fibo(n):
    global num1, num2, num3 #글로벌 없으면 지역변수를 못찾기때문에 에러
    fibolist = [] # 지역변수 아무것도 안나옴. 출려은 전역변수 fibolist[]를 출력하기때문
    fibolist.append(num1) #fibolist = 0,1,1
    fibolist.append(num2)
    fibolist.append(num3)
    for i in range(3, n) :# 3부터 n-1까지 for문 돌림
        num1 = num2
        num2 = num3
        num3 = num1 + num2
        fibolist.append(num3)
    

fibolist = []
num1 = 0
num2 = 1
num3 = 1
num = int(input("피보너치 수열을 구할 갯수를 입력하세요. 단 3이상의 값:"))
print("f(",num,")=",end="")
fibo(num)
print(fibolist)
