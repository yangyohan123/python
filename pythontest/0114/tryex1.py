'''
Created on 2020. 1. 14.

@author: GDJ-19
예외처리 예제
'''
mystr = "파이썬 공부 중입니다. 열심히 파이썬을 공부합시다."
strpos = [] #파이썬문자의 위치
index = 0
while True :
    #index 이후의 파이썬문자열의 위치
    try :
        index = mystr.index("파이썬",index) 
        #  strpos.\ : 두줄을 한줄로 연결 표시
        strpos.\
        strpos.append(index)
        index += 1
    except :
        break
print("파이썬의 문자 위치:" ,strpos,",문자 갯수:",len(strpos))
