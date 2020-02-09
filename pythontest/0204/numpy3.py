'''
Created on 2020. 2. 4.

@author: GDJ-19
'''
import numpy as np

x = np.random.randint(10, size = 10) #[0, 1, 2, 3, 4, 5, 6, ,7 ,8, 9]
x_sub = x[:2]
print(x)
print(x_sub)
x_sub[0] = 20 #사본(x_sub)의 0번째 요소를 20으로 바꾸면 원본(x)도 바뀜
print(x)
print(x_sub)

x_cop = x.copy()
x_cop[0] = 100
print(x)
print(x_cop)

#배열의 재편성 : 10개의 요소를 2차원배열 (5,2)로 재편성
x2 = x.reshape(5,2)
print(x2)

#0부터 9까지의 임의의 수를 9개로 이루어진 배열 생성하기.
#9개의 배열을 3행 3열 배열로 재편성하기.
x = np.random.randint(10, size= 9)
x3 = x.reshape(3,3)
print(x3)