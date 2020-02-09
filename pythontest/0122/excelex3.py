'''
Created on 2020. 1. 28.

@author: GDJ-19
xls : pip install xlrd
'''

from xlrd import open_workbook

input_file = "ssec1804.xls"
workbook = open_workbook(input_file)

print("worksheets의 갯수:",workbook.nsheets)
for worksheet in workbook.sheets() :
    print("worksheet 이름 :", worksheet.name,"\n 행수:",
          worksheet.nrows, "\n컬럼수:",worksheet.ncols)
    