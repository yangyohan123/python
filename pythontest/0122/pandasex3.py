'''
Created on 2020. 1. 22.

@author: GDJ-19
'''
import pandas as pd

input_file = "supplier_data.csv"
output_file = "pandas_out2.csv"

data_frame = pd.read_csv(input_file)
data_frame_in_set =\
data_frame.loc[data_frame["Invoice Number"].
                str.startswith("001-")]
print(data_frame_in_set)

#선택된 데이터 csv 파일로 저장
data_frame_in_set.to_csv(output_file, index=False)
