'''
Created on 2020. 2. 4.

@author: GDJ-19
'''
import numpy as np

print(np.array([1,4,2,5,3]))
print(np.array([3.14,4,2,3]))
print(np.array([1,2,3,4],dtype="float32"))

#기본 함수
arr = np.zeros(10,dtype=int) # 10개의 요소를 0으로 채움
print(arr)
arr = np.ones((3,5), dtype=float) # 3행 5열 리스트 생성. 1로 채움
print(arr)
arr = np.full((3,5),3.14) #3행 5열 리스트 생성. 3.14로 채움
print(arr)
# 0에서 시작해 2씩 더해 20까지 채우는 배열 생성
arr = np.arange(0, 20 ,2)
print(arr)

#0과 1 사이에 일정한 간격을 가진 다섯 개의 값으로 채운 배열 만들기
arr = np.linspace(0, 1, 5)
print(arr)

#3*3 크기의 난수 배열 생성
arr = np.random.random((3,3))
print(arr)

#평균0, 표준 편차 1의 정규 분포를 따르는 #*3 난수 배열
arr = np.random.normal(0, 1, (3,3))
print(arr)

# [0,10] 구간의 임의로 정수로 채운 3*3 배열 만들기
arr = np.random.randint(0, 10, (3,3))
print(arr)


print(arr.ndim) # 배열의 차원 리턴
print(arr.shape) # 각 차원의 크기 리턴
print(arr.size) # 전체 배열의 크기. 전체 요소의 갯수 . 3*3
print(arr.dtype) # 배열 요소의 자료형