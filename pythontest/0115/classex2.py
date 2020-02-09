'''
Created on 2020. 1. 15.

@author: GDJ-19
'''




class Car :
    color = ""
    speed = 0
    count = 0
    num = 0
    def __init__(self): #생성자
        self.speed = 0 #인스턴스 변수
        Car.count += 1 #클래스 변수 모든 객체가 공유하는 변수
        self.num = Car.count
        
    def printMessage(self):
        print("printMessage 메서드 호출됨")
        
mycar1, mycar2 = None,None
mycar1 = Car()
mycar1.speed = 30
print("자동차1 : 속도 = %d, 번호 %d, 생산된 자동차수량: %d" %(mycar1.speed,mycar1.num,mycar1.count))
mycar2 = Car()
mycar2.speed = 50
print("자동차1 : 속도 = %d, 번호 %d, 생산된 자동차수량: %d" %(mycar1.speed,mycar1.num,mycar1.count))
print("자동차1 : 속도 = %d, 번호 %d, 생산된 자동차수량: %d" %(mycar2.speed,mycar2.num ,mycar2.count))