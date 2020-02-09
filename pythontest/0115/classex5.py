'''
Created on 2020. 1. 17.

@author: GDJ-19
추상메서드 예제
'''
class SuperClass :
    #추상메서드
    def method(self):
        raise NotImplementedError # 반드시 오버라이드 해야 함
    
class SubClass1(SuperClass):
    def method(self):
        print("Subclass1에서 method()를 오버라이딩 함")
class SubClass2(SuperClass):
    def method(self):
        print("SubClass2에서 method()를 오버라이딩 함")


sub1 = SubClass1()
sub2 = SubClass2()

sub1.method()
sub2.method()