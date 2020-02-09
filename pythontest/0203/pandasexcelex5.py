'''
Created on 2020. 1. 28.

@author: GDJ_19
'''


import pandas as pd

input_file = "sales_2013.xlsx"
output_file = "pandas_output5.xls"
data_frame = pd.read_excel\
         (input_file,sheet_name=None,index_col=None)
                #data_frame_value : 조건에맞는 데이터저장

#list
row_output =[]



# data_frame : 모든 시트를 가지고 있음
# items : 시트 데이터들을 가져옴
for worksheet_name, data in data_frame.items() :
    # data : sheet 내용 저장
    print("====",worksheet_name,"====")
    #replace('$','').replace(',', '') : $와 ,를 없앰
    #astype(float) : float type로 바꿈
    # > 2000.0 : 2000이 상인 애들만 가져옴
    row_output.append(data[data['Sale Amount'].replace('$','').replace(',', '').astype(float) > 2000.0])
#for 구문 종료
# axis=0 : row로 추가
# axis=1 : colum로 추고
filtered_row = pd.concat\
    (row_output,axis=0, ignore_index=True)
writer = pd.ExcelWriter(output_file)
filtered_row.to_excel\
    (writer, sheet_name="sale_amount_gt2000",index=False)
writer.save()