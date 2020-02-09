'''
Created on 2020. 1. 17.

@author: GDJ-19
상속예제, 오버라이딩.
다중상속 가능 => 자손클래스의 부모클래스가 여러개 가능
'''
class Car :
    speed = 0
    def upSpeed(self, value):
        self.speed  += value
        print(", 현재 속도(부모클래스) : %d"% self.speed)

class Sedan(Car): #상속표현
    pass          #추가되는 멤버 없는 경우

class Truck(Car):
    def upSpeed(self, value): # Car의 upSpeed, self: 인스턴스 변수, 오버라이딩
        self.speed += value
        if self.speed > 150 :
            self.speed = 150
            print("현재 속도(자손 클래스) : %d"% self.speed)

class Container :
    room = 1
    
class MovingCar(Car, Container): # 다중상속(Car,Container)
    pass
sedan1, truck1 = None, None
truck1 = Truck()
sedan1 = Sedan()
mcar = MovingCar()
print("이동차량의 방갯수:",mcar.room, end="")
mcar.upSpeed(60)
print("트럭->", end="")
truck1.upSpeed(200)
print("승용차->", end="")
sedan1.upSpeed(200)