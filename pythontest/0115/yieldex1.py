'''
Created on 2020. 1. 20.

@author: GDJ-19
yield : 함수의 종료 없이, yield 에악어로 값 리턴
'''
#함수의 종료 : 리턴값이나 문장의 마지막을 만나면 종료함.

def genFun(num):
    for i in range(10, num + 10) :
        #중간값을 계속 전달 종료없이.
        #호출한 메서드에게 값들을 전달
        yield(i)
        print(i, "값 반환")

#type : generator
#print(type(genFun(5)))
#print(list(genFun(5)))

for i in list(genFun(5)):
    print(i)