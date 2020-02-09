'''
Created on 2020. 1. 21.

@author: GDJ-19

euc-kr로 코딩된 jeju1.csv를 utf8로 변경하여 데이터 출력
'''
import codecs
filename = "jeju1.csv"
csv = codecs.open(filename, "r","euc-kr").read()
data = []
rows = csv.split("\r\n")
for row in rows :
    if row == "" : continue # 입력줄이 공백
    cells = row.split(",")
    data.append(cells) 

outfp = open("jeju1.txt", "w", encoding='UTF8')
for c in data :
    print(c[0], c[1], c[2])
    outfp.write(" ".join(map(str,c))+ "\n")