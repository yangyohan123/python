'''
Created on 2020. 1. 9.

@author: GDJ-19
문자열 처리하기
문자열 배열 처리 가능함.
'''
print("안녕하세요")
print("안녕하세요"[0]) #0번 인덱스 문자 출력하기 - 안
print("안녕하세요"[4]) #4번 인덱스 문자 출력하기 - 요
print("안녕하세요"[-1]) #뒤에서 첫번째 문자 출력 - 요
print("안녕하세요"[-2]) #뒤에서 두번째 문자 출력 - 세

#부분문자열
print("안녕하세요"[1:3]) #1번인덱스부터 2번인덱스까지 부분문자열 출력 - 녕하
print("안녕하세요"[:3]) #0번인덱스부터 2번인덱스까지 부분문자열 출력 - 안녕하
print("안녕하세요"[3:]) #3번인덱스부터 끝까지 부분문자열 출력 - 세요
print("안녕하세요"[::2]) #0번인덱스부터 2씩 증가하여 부분문자열 출력
print("안녕하세요"[::-1]) #역순으로 출력.
print(type("안녕하세요"))
print("'안녕하세요' 문자열 길이",len("안녕하세요"))
print(type(len))

a = "hello"
cnt = 0
for i in range(0,len(a)) :
    if a[i] == "l" :
        cnt += 1
    
print("hello에  l의 문자의 개수=%d"%cnt)
print("hello에  l의 문자의 개수=%d"%a.count('h'))
print("hello에  l의 문자의 개수=%d"%a.find('l'))
print("hello에  l의 문자의 개수=%d"%a.find('a')) #없을 경우: -1을 반환
print("hello에  l의 문자의 개수=%d"%a.index('l'))
print("hello에  l의 문자의 개수=%d"%a.index('a')) #없을 경우 : 에러반환
