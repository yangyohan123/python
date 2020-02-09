'''
Created on 2020. 1. 22.

@author: GDJ-19
'''
import pandas as pd
df = pd.DataFrame({'A':[1,4,7], 'B':[2,5,8],
                   'C':[3,6,9]})

print(type(df))
print(df)

#0번 인덱스 값 조회하기
print(df.iloc[0])
print(df.iloc[1])
print(df.loc[0])
print(df.ix[0])
'''
    행 선택: iloc : 순서기준
          loc : 이름 기준
    열 선택: df['A']

'''

print(df['A'])
df = pd.DataFrame(data=([[1,2,3],[4,5,6],[7,8,9]]),
                  index=[2,"A",4],columns=[51,52,54])
print(df)

''' iloc => 인덱스 기준, 순번 , 순서기준'''

print("df.iloc[2]=>")
print(df.iloc[2])

''' loc => 인덱스 이름 기준'''
print("df.loc[2]=>")
print(df.loc[2])