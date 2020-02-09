'''
Created on 2020. 1. 9.

@author: GDJ-19
초를 입력받아 몇시간 몇분 몇초인지 출력하기
'''

time = int(input("초:"))
hour = time//3600
time %= 3600
minute = time//60
second = minute%60
print("""%d 시간 %d 분 %d 초"""% (hour,minute,second))