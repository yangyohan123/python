'''
Created on 2020. 2. 3.

@author: GDJ-19
'''
import pandas as pd 
input_file="sales_2013.xlsx"
output_file = "pandas_output4.xls"
data_frame = pd.read_excel\
             (input_file,"january_2013",index_col=None)

data_frame_value = data_frame.loc\
                    [:,["Customer ID","Sale Amount","Purchase Date"]]
                
writer = pd.ExcelWriter(output_file)
data_frame_value.to_excel\
                (writer,sheet_name="jan_13_output",index=False)

#저장
writer.save()