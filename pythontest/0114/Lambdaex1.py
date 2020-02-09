'''
Created on 2020. 1. 14.

@author: GDJ-19
람다식으로 함수 구현하기
람다식으로 함수 구현하기
람다 : 함수객체
'''


def hap(num1,num2): #정적으로 hap이란 함수는 두 수의 더하는걸로 지정.
                    #
    res = num1 + num2
    return res

print(hap(10,20))


hap2 = lambda num1,num2:num1*num2 # 동적으로 처리
print(hap2(10,20))

hap2 = lambda num1,num2:num1+num2
print(hap2(10,20))

#매개변수에 기본값 설정하기
hap3 = lambda num1=0,num2=1:num1+num2
print(hap3())
print(hap3(100))
print(hap3(100,200))