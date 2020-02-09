'''
Created on 2020. 1. 10.

@author: GDJ-19
functionex3.py : 전역 변수 사용하기
'''
def func1() :
    global gval # 전역변수 gval으로 만들어줌
    gval = 200 
    a = 20 # 지역 변수
    b = 1000 # 지역 변수
    print("func1() 함수 호출함", gval, a,b)
    
def func2():
    b = 2000 #지역변수
    print("func2() 함수에서 func1() 함수를 호출함")
    func1()
    print("전역 변수 gval 값=",gval, a,b)
#전역변수  => 모든 함수에서 사용이 가능한 변수
gval =100
a =10


#main
#방법1 
 #func2()

#방법2 
if __name__ == '__main__' : #프로그램의 시작점.
    func2()
