'''
Created on 2020. 1. 21.

@author: GDJ-19
jeju1.csv의 파일내용 복사하여 jeju1_bak.csv 붙여넣기
'''
import sys # command 라인에서 입력값 받기
input_file = sys.argv[1] #jeju1.csv
output_file = sys.argv[2] #jeju1_bak.csv
with open(input_file, 'r', newline="") as filereader :
    with open(output_file, 'w', newline="") as filewriter :
        header = filereader.readline()
        header = header.strip() #공백제거
        print(header)
        header_list = header.split(",")
        print(header_list)
        filewriter.write(",".join(map(str, header_list))
                         + "\r\n")
        for row_list in filereader :
            filewriter.write("".join(map(str, row_list)))