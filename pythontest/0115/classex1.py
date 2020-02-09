'''
Created on 2020. 1. 15.

@author: GDJ-19
클래스예제
'''
# 기본 생성자 : __init__(self) : 구현된 생성자가 없는 경우
#                            시스템이 제공하는 생성자

class Car :
    color = ""
    speed = 0
    def __init__(self,v1,v2): # 생성자
        self.color = v1
        self.speed = v2
        
    def upSpeed(self, value): # 메서드
        self.speed += value
    def downSpeed(self, value): # 메서드
        self.speed -= value


myCar1 = Car("빨강",0) # 객체화
#myCar1.color = "빨강"
#myCar1.speed = 0
myCar1.upSpeed(30)
print("자동차의 색상은 %s 이며, 현재 속도는 %dkm 입니다."
      % (myCar1.color, myCar1.speed))


myCar2 = Car("파랑",50) # 객체화
myCar2.downSpeed(20)
print("자동차의 색상은 %s 이며, 현재 속도는 %dkm 입니다."
      % (myCar2.color, myCar2.speed))