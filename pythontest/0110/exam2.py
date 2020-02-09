'''
Created on 2020. 1. 10.

@author: GDJ-19
'''
ss = "홍길동"
# 홍#길#동# 으로 출력하기
for i in range(0,len(ss)) : 
    print(ss[i],end="#")

print()
# 동길홍으로 출력하기
for i in range(len(ss)-1,-1,-1) :
    print(ss[i],end="")
    
print()
print(ss[::-1])

# ss 문자열이 '('시작하지 않으면 '('추가하기. '('시작하면 추가하지 않음.
#           ')'끝나지 않으면 ')'추가하기.
# (홍길동) 출력하기

if ss.startswith("(") == False :
    print("(",end="")
print(ss,end="")
if ss.endswith(")") == False :
    print(")")
    
ss = "2020/01/10"
print("ss 날짜의 10년 전을 출력하기")
list = ss.split("/") #['2020', '01', '10'] 리스트형태로 만들어줌
print(int(list[0])-10,"년",list[1],"월",list[2],"일")
print(list)
