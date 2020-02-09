'''
Created on 2020. 2. 3.

@author: GDJ-19
'''
#import pandas 모듈을 pd로 사용
import pandas as pd

# 읽을 파일
input_file = "sales_2013.xlsx"

# 출력 파일
output_file = "pandas_output3.xls"

#data_frame : sales_2013.xlsx 파일의 "january_2013" 모든 내용을 저장 
#read_excel : 엑셀파일 읽음
#sheet : january_2013
#index_col-None : 인덱스는 없음
data_frame = pd.read_excel\
             (input_file,"january_2013",index_col=None)
             

select_date = ['01/24/2013','01/31/2013']

#isin : select_date 속한 값이 경우만 선택
#data_frame_value : 01/24/2013, 01/31/2013 날짜에 해당하는 모든 데이터
data_frame_value = \
                    data_frame[data_frame['Purchase Date'].isin(select_date)]

#writer에 pandas_output3.xls 파일을 가지고 잇음
writer = pd.ExcelWriter(output_file)

#pandas_output3.xls
#sheet : "jan_13_output"
#
data_frame_value.to_excel\
                (writer,sheet_name="jan_13_output",index=False)

#저장
writer.save()