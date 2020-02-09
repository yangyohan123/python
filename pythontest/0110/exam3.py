'''
Created on 2020. 1. 10.

@author: GDJ-19
배열의 값의 합과 평균을 구하는 함수 작성하기
'''
def getSum(list):
    # 방법 1
    res = 0 
    for i in range (0,len(list)) :
        res += list[i]
    return res
    
    #방법2
    return sum(list)
def getMean(list):
    #원래 한줄에 사용되는 경우 표시 '\' : 연결문자
    # 방법1
    mean = getSum(list)/len(list) \
        if len(list) > 0 else 0
    return mean
    # 방법2
    return sum(list)/len(list) \
        if len(list) > 0 else 0
    
list = [2,3,3,4,4,5,5,6,6,8,8] # list
list2 = []
tp = (2,3,3,4,4,5,5,6,6,8,8) #튜플

print("list의 값의 합:", getSum(list))
print("list의 값의 평균:", getMean(list))

print("list2의 값의 합:", getSum(list2))
print("list2의 값의 평균:", getMean(list2))

print("tp의 값의 합:", getSum(tp))
print("tp의 값의 평균:", getMean(tp))
