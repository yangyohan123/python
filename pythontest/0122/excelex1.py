'''
Created on 2020. 1. 22.

@author: GDJ-19

xlsx : x=>xml, pip install penpyxl 
xls :          pip install xlrd

'''

import openpyxl #pip install openpyxl

filename = "sales_2015.xlsx"
book = openpyxl.load_workbook(filename)
sheet = book.worksheets[0] # 첫번째 sheet 선택 
data = []
for row in sheet.rows :
    line = []
    # l : 열의 번호
    # d : 값을 의미함.
    for l, d in enumerate(row) :
        line.append(d.value)
#        print(l,end="\t")
    print(line) #
    data.append(line) # list형태의 data가 됨
print(type(data))
print(data)

# enumerate : 리스트에서 데이터와 index값을 제공
# i : 인덱스
# a : 값을 의미함
for i,a in enumerate(data) :
    if (i >= 10) :
        break;
    print(i+1, a)