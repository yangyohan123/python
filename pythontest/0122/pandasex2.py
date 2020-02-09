'''
Created on 2020. 1. 22.

@author: GDJ-19
pasdas 모듈을 이용하여 csv 파일을 읽고 쓰기
supplier_data.csv 다운받기
'''

import pandas as pd

input_file = "supplier_data.csv"
output_file = "pandas_out1.csv"

data_frame = pd.read_csv(input_file)
print(type(data_frame))
print(data_frame)
print("===============================")
important_dates = ["1/20/14","1/30/14"]
'''
data_frame_in_set : Purchase Data 열의 값이 
                    "1/20/14","1/30/14" 값에 속한 모든 컬럼 조회
loc => 행 선택 ,  Purchase Date행에서 
isin(important_dates)=> "1/20/14","1/30/14"인 것들의  
(, :) => 모든 열을 가져옴
'''
data_frame_in_set =\
data_frame.loc[data_frame["Purchase Date"].
                isin(important_dates), :]
print(data_frame_in_set)

#선택된 데이터 csv 파일로 저장
data_frame_in_set.to_csv(output_file, index=False)
