'''
Created on 2020. 1. 21.

@author: GDJ-19


open(파일이름, 파일모드, [인코딩방식])

파일 모드
 "r" : 읽기 모드
 "w" : 쓰기 모드, 파일이 존재하지 않으면 생성
 "r+" : 읽기/쓰기 겸용모드
 "a" : 쓰기 모드, append 모드. 파일이 존재하지 않으면 생성
           존재하는 경우는 기존 내용 이후에 추가됨.
 "t" : 텍스트 모드. 기본형
 "b" : 이진 모드
'''

infp = None
inStr = ""
# file을 열 때 한글을 encoding="UTF8"로 인코딩
infp = open("../0115/regularex3.py","rt",encoding="UTF8")
while True :
    #infp.readline() 한줄을 읽고 inStr에 저장
    inStr = infp.readline()
    if inStr == None : #EOF(End Of File)상태
        break
    print(inStr, end="")

infp.close()