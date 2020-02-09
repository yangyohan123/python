'''
Created on 2020. 2. 3.

@author: GDJ-19
'''
import pandas as pd
input_file = "sales_2013.xlsx"
output_file = "pandas_output7.xls"

my_sheets=[0,1] # 첫번재 sheet, 두번째 sheet만 선택
threshold=1900.0
data_frame = pd.read_excel\
            (input_file,sheet_name=my_sheets,index_col=None)
row_list=[]

#선택된 sheet의 내용 중 Sale Amount의 값이 1900보다 많은 값을 가진 행을 선택
for worksheet_name, data in data_frame.items() :
    row_list.append(data[data["Sale Amount"].\
                        replace("$","").replace(",","").astype(float)> threshold])
    
filtered_row = pd.concat\
                (row_list, axis=0, ignore_index=True)
writer = pd.ExcelWriter(output_file)
filtered_row.to_excel\
(writer,sheet_name="set_of_worksheets", index=False)
writer.save()