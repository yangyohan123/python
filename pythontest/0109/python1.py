'''
Created on 2020. 1. 9.

@author: GDJ-19
1.변수 선언 필요 없음.
2.  { } 블럭이 없음.
    if, 반복문내부에서 블록표시가 없다. => 공백으로 블록 표시
3. ''' ''' 여러줄 주석
   #       한줄 주석
'''
sel = int(input('입력 진수 결정(16/10/8/2) :'))#16
num = input("값 입력: ") # 10
if sel == 16 : # 블럭시작
        num10 = int(num,16)
#블럭종ㄹ
if sel == 10 :
        num10 = int(num,10)
if sel == 8 :
        num10 = int(num,8)
if sel == 2 :
        num10 = int(num,2)
print(num10)

#10진수를 진법으로 출력
print("16진수=>", hex(num10))
print("8진수=->", oct(num10))
print("2진수=>", bin(num10))
