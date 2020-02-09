'''
Created on 2020. 1. 28.

@author: GDJ-19
excel 파일을 pandas로 읽기
'''

import pandas as pd #pip install pandas

input_file = "sales_2015.xlsx"
output_file = "pnadas_output.xls"

data_frame = pd.read_excel\
                (input_file,"january_2015",index_col=None)
#data_frame_value : 조건에 맞는 데이터 저장
data_frame_value = \
                    data_frame[data_frame['Sale Amount'].astype(float) > 300.0]
writer = pd.ExcelWriter(output_file)
data_frame_value.to_excel(writer,
                          sheet_name="jan_15_output", index=False)

writer.save()
