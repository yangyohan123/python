'''
Created on 2020. 1. 9.

@author: GDJ-19
삼각형의 높이를 입력받은 후 삼각형을 출력하는 프로그램 작성
'''


num = int(input("삼각형의 높이:"))

for i in range(0,num+1) :
    print("*"*i)
print()

for i in range(num,0,-1) :
    print("*"*i)
print()

for i in range(0,num+1) :
    print(" "*(num-i),end="")
    print("*"*i)

print()
for i in range(0,num+1) :
    print(" "*(num-i),end="")
    print("*"*(i*2-1))