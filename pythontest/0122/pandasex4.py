'''
Created on 2020. 1. 22.

@author: GDJ-19
'''
import pandas as pd
input_file = "supplier_data.csv"
output_file = "pandas_out3.csv"

df = pd.read_csv(input_file)
df_col = df.iloc[:,[0,3]] #0번열과 3번열 조회
''' 0번 : Supplier Name, 3번 : Cost'''
print("=====df.iloc[:,[0,3]]======")
print(df_col)
df_col = df.iloc[0:4,0:3]
print("=====df.iloc[0:4,0:3]====")
print(df_col)
# 모든 행의 Invoice Number, Cost 컬럼 조회
df_col = df.loc[:, ["Invoice Number","Cost"]]
print("=====df.loc[:, ['Invoice Number','Cost]]=======")
print(df_col)

# Invoice Number의 값이 920- 시작하는 행의
# Invoice Number, Cost 컬럼 조회
df_col = df.loc[df["Invoice Number"].str.startswith("920-"),["Invoice Number","Cost"]]
print(df_col)
df_col.to_csv(output_file, index=False)
